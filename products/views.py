from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower

from .models import Product, Category, Wishlist, WishlistItem, Review
from .forms import ProductForm, ReviewForm
from profiles.models import UserProfile


def all_products(request):
    products = Product.objects.all().annotate(avg_rating=Avg('reviews__rating'))
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details and reviews """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product).order_by('-created_at')

    avg_rating = reviews.filter(rating__gte=1, rating__lte=5).aggregate(Avg('rating'))['rating__avg']
    avg_rating = round(avg_rating) if avg_rating else 0 

    context = {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating,  
        'review_form': ReviewForm(),
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def submit_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review, created = Review.objects.update_or_create(
                product=product, user=request.user,
                defaults={'rating': form.cleaned_data['rating']}
            )
            if created:
                messages.success(request, "Your rating has been submitted.")
            else:
                messages.success(request, "Your rating has been updated.")
        else:
            messages.error(request, "There was an error submitting your rating.")

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    messages.success(request, "Your review has been deleted.")
    return redirect(reverse('product_detail', args=[review.product.id]))


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_profile = request.user.userprofile

    wishlist, created = Wishlist.objects.get_or_create(
        user_profile=user_profile,
        name="My Wishlist"
    )

    WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)

    messages.success(request, f'Added {product.name} to your wishlist.')
    return redirect(reverse('view_wishlist'))


@login_required
def view_wishlist(request):
    user_profile = request.user.userprofile
    wishlist = Wishlist.objects.filter(user_profile=user_profile, name="My Wishlist").first()

    if not wishlist:
        wishlist = Wishlist.objects.create(
            user_profile=user_profile,
            name="My Wishlist"
        )

    context = {
        'wishlist': wishlist,
    }
    return render(request, 'products/wishlist.html', context)


@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(WishlistItem, pk=item_id,
                             wishlist__user_profile=request.user.userprofile)
    item.delete()
    messages.success(request, 'Item removed from your wishlist.')
    return redirect(reverse('view_wishlist'))
