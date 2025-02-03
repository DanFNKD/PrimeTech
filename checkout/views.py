from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents
import stripe
import json


@require_POST
def cache_checkout_data(request):
    """Store checkout metadata in Stripe"""
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid, metadata={
                'bag': json.dumps(request.session.get('bag', {})),
                'save_info': request.POST.get('save_info'),
                'username': '' if not request.user.is_authenticated
                else request.user.username,
            }
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request, "Sorry, your payment cannot be processed right now. "
            "Please try again later."
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """Handles checkout process"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            key: request.POST[key] for key in [
                'full_name', 'email', 'phone_number', 'country',
                'postcode', 'town_or_city', 'street_address1',
                'street_address2', 'county',
            ]
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        OrderLineItem.objects.create(
                            order=order, product=product, quantity=item_data
                        )
                except Product.DoesNotExist:
                    messages.error(
                        request, "One of the products in your bag wasn't found"
                        "in our database. Please call us for assistance!"
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))

        messages.error(
            request, "There was an error with your form. "
            "Please double-check your information."
        )

        return render(request, 'checkout/checkout.html', {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': '',
        })

    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe_secret_key = stripe_secret_key or 'sk_test_dummy'
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request, "Stripe public key is missing. "
            "Did you forget to set it in your environment?"
        )

    return render(request, 'checkout/checkout.html', {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    })


def checkout_success(request, order_number):
    """Handles successful checkouts"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    subject = f"Order Confirmation - {order.order_number}"
    message = (
        f"Thank you for your order!\n\n"
        f"Your order number is {order.order_number}.\n"
        f"A confirmation email has been sent to {order.email}.\n\n"
        f"Thank you for shopping with us at PrimeTech!"
    )

    send_mail(
        subject, message, settings.DEFAULT_FROM_EMAIL, [order.email],
        fail_silently=False
    )


    messages.success(
        request,
        f"Order successfully processed! Your order number is "
        f"{order.order_number}. A confirmation email has been sent to "
        f"{order.email}."
    )


    if 'bag' in request.session:
        del request.session['bag']


    return render(request, 'checkout/checkout_success.html', {'order': order})