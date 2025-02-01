from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.db.models import Avg
from .models import Product, Category, Wishlist, WishlistItem, Review
from .forms import ReviewForm
from profiles.models import UserProfile

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics", friendly_name="Electronics")
        self.product = Product.objects.create(
            category=self.category,
            sku="ABC123",
            name="Test Product",
            description="A test product.",
            price=Decimal("100.00"),
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), "Test Product")

    def test_update_rating_no_reviews(self):
        self.product.update_rating()
        self.assertIsNone(self.product.rating)

    def test_update_rating_with_reviews(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        Review.objects.create(product=self.product, user=user1, rating=4)
        Review.objects.create(product=self.product, user=user2, rating=2)
        self.product.update_rating()
        self.assertEqual(self.product.rating, 3.0)

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Tech", friendly_name="Technology")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Tech")

    def test_get_friendly_name(self):
        self.assertEqual(self.category.get_friendly_name(), "Technology")

class WishlistModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="wishuser", password="pass123")
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        self.wishlist = Wishlist.objects.create(user_profile=self.profile, name="My Wishlist")

    def test_wishlist_str(self):
        expected = f"My Wishlist ({self.user.username})"
        self.assertEqual(str(self.wishlist), expected)

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="reviewer", password="pass123")
        self.category = Category.objects.create(name="Tech", friendly_name="Technology")
        self.product = Product.objects.create(
            category=self.category,
            sku="SKU1",
            name="Review Product",
            description="Review product description",
            price=Decimal("120.00"),
        )

    def test_review_str(self):
        review = Review.objects.create(product=self.product, user=self.user, rating=5)
        expected = f"{self.user.username} rated {self.product.name} 5★"
        self.assertEqual(str(review), expected)

class AllProductsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Tech", friendly_name="Technology")
        Product.objects.create(
            category=self.category,
            sku="SKU1",
            name="Product 1",
            description="Desc 1",
            price=Decimal("50.00"),
        )
        Product.objects.create(
            category=self.category,
            sku="SKU2",
            name="Product 2",
            description="Desc 2",
            price=Decimal("75.00"),
        )

    def test_all_products_view(self):
        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)
        self.assertEqual(len(response.context['products']), 2)

class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Tech", friendly_name="Technology")
        self.product = Product.objects.create(
            category=self.category,
            sku="SKU1",
            name="Product Detail",
            description="Product detail description",
            price=Decimal("100.00"),
        )

    def test_product_detail_view(self):
        url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(response.context['product'], self.product)
        self.assertIn('review_form', response.context)

class SubmitReviewViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Tech", friendly_name="Technology")
        self.product = Product.objects.create(
            category=self.category,
            sku="SKU1",
            name="Review Product",
            description="Review product description",
            price=Decimal("120.00"),
        )
        self.user = User.objects.create_user(username="reviewer", password="pass123")
        self.client.login(username="reviewer", password="pass123")

    def test_submit_review_valid(self):
        url = reverse('submit_review', args=[self.product.id])
        data = {'rating': '5'}
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('product_detail', args=[self.product.id]))
        self.assertEqual(Review.objects.filter(product=self.product, user=self.user).count(), 1)

    def test_submit_review_invalid(self):
        url = reverse('submit_review', args=[self.product.id])
        data = {'rating': '10'}
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('product_detail', args=[self.product.id]))
        self.assertEqual(Review.objects.filter(product=self.product, user=self.user).count(), 0)

class WishlistViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="wishlistuser", password="pass123")
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        self.client.login(username="wishlistuser", password="pass123")
        self.category = Category.objects.create(name="Tech", friendly_name="Technology")
        self.product = Product.objects.create(
            category=self.category,
            sku="SKU1",
            name="Wishlist Product",
            description="Wishlist product description",
            price=Decimal("80.00"),
        )

    def test_add_to_wishlist(self):
        url = reverse('add_to_wishlist', args=[self.product.id])
        response = self.client.get(url)
        self.assertRedirects(response, reverse('view_wishlist'))
        wishlist = self.profile.wishlists.first()
        self.assertIsNotNone(wishlist)
        self.assertTrue(wishlist.items.filter(product=self.product).exists())

    def test_view_wishlist(self):
        Wishlist.objects.get_or_create(user_profile=self.profile, name="My Wishlist")
        url = reverse('view_wishlist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/wishlist.html')
        self.assertIn('wishlist', response.context)

    def test_remove_from_wishlist(self):
        wishlist, _ = Wishlist.objects.get_or_create(user_profile=self.profile, name="My Wishlist")
        wishlist_item = WishlistItem.objects.create(wishlist=wishlist, product=self.product)
        url = reverse('remove_from_wishlist', args=[wishlist_item.id])
        response = self.client.get(url)
        self.assertRedirects(response, reverse('view_wishlist'))
        self.assertFalse(wishlist.items.filter(id=wishlist_item.id).exists())

class ReviewFormTest(TestCase):
    def test_review_form_valid(self):
        form_data = {'rating': '4'}
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_review_form_invalid(self):
        form_data = {'rating': '10'}
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)
