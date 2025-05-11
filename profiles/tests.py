from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order


class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='pass123'
        )
        self.profile = UserProfile.objects.get(user=self.user)
        self.url = reverse('profile')
        self.client.login(username='testuser', password='pass123')

    def test_profile_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertIn('form', response.context)
        self.assertIn('orders', response.context)
        self.assertTrue(response.context.get('on_profile_page'))

    def test_profile_view_post_valid(self):
        post_data = {
            'default_phone_number': '1234567890',
            'default_street_address1': '123 Test St',
            'default_street_address2': 'Apt 1',
            'default_town_or_city': 'Test City',
            'default_county': 'Test County',
            'default_postcode': '12345',
            'default_country': 'US'
        }
        response = self.client.post(self.url, data=post_data)
        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_phone_number, '1234567890')
        self.assertEqual(self.profile.default_street_address1, '123 Test St')
        self.assertIn('US', str(self.profile.default_country))

    def test_profile_view_post_invalid(self):
        post_data = {
            'default_phone_number': '1' * 25,
            'default_street_address1': '123 Test St',
            'default_street_address2': 'Apt 1',
            'default_town_or_city': 'Test City',
            'default_county': 'Test County',
            'default_postcode': '12345',
            'default_country': 'US'
        }
        response = self.client.post(self.url, data=post_data)
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertTrue(
            any(
                "failed" in str(message).lower()
                for message in messages
            )
        )


class OrderHistoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser2',
            password='pass123'
        )
        self.profile = UserProfile.objects.get(user=self.user)
        self.order = Order.objects.create(
            full_name="Test User",
            email="test@example.com",
            phone_number="1234567890",
            country="US",
            postcode="12345",
            town_or_city="Test City",
            street_address1="123 Test St",
            street_address2="Apt 1",
            county="Test County",
            delivery_cost='10.00',
            order_total='100.00',
            grand_total='110.00',
            original_bag="{}",
            stripe_pid="dummy_pid"
        )
        self.order.user_profile = self.profile
        self.order.save()
        self.url = reverse('order_history', args=[self.order.order_number])
        self.client.login(username='testuser2', password='pass123')

    def test_order_history_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertIn('order', response.context)
        self.assertTrue(response.context.get('from_profile'))
