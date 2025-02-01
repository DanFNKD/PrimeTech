import json
import time
from decimal import Decimal
from unittest.mock import patch, MagicMock

from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from django.contrib.messages import get_messages

from checkout.models import Order, OrderLineItem
from checkout.forms import OrderForm
from checkout.views import checkout, cache_checkout_data, checkout_success
from checkout.webhooks import webhook
from products.models import Product
from profiles.models import UserProfile

class CacheCheckoutDataViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        session = self.client.session
        session['bag'] = {'1': 2}
        session.save()

    @patch('checkout.views.stripe.PaymentIntent.modify')
    def test_cache_checkout_data_success(self, mock_modify):
        fake_client_secret = 'pi_12345_secret_67890'
        data = {
            'client_secret': fake_client_secret,
            'save_info': 'on',
        }
        url = reverse('cache_checkout_data')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        pid = fake_client_secret.split('_secret')[0]
        mock_modify.assert_called_with(pid, metadata={
            'bag': json.dumps(self.client.session.get('bag', {})),
            'save_info': data.get('save_info'),
            'username': '',
        })

    @patch('checkout.views.stripe.PaymentIntent.modify', side_effect=Exception("Test error"))
    def test_cache_checkout_data_failure(self, mock_modify):
        fake_client_secret = 'pi_12345_secret_67890'
        data = {
            'client_secret': fake_client_secret,
            'save_info': 'on',
        }
        url = reverse('cache_checkout_data')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)

class CheckoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name="Test Product",
            price=Decimal("50.00"),
        )
        session = self.client.session
        session['bag'] = {str(self.product.pk): 2}
        session.save()

    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_checkout_get(self, mock_create):
        fake_intent = MagicMock()
        fake_intent.client_secret = 'secret_test'
        mock_create.return_value = fake_intent
        url = reverse('checkout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertEqual(response.context['client_secret'], fake_intent.client_secret)

    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_checkout_post_valid_form(self, mock_create):
        fake_intent = MagicMock()
        fake_intent.client_secret = 'secret_test'
        mock_create.return_value = fake_intent
        url = reverse('checkout')
        post_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '123456789',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'Test City',
            'street_address1': '123 Test St',
            'street_address2': '',
            'county': 'Test County',
            'client_secret': 'pi_test_secret_test',
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 302)
        order = Order.objects.first()
        self.assertIsNotNone(order)
        self.assertEqual(order.full_name, 'Test User')
        self.assertEqual(order.lineitems.count(), 1)

    def test_checkout_post_invalid_form(self):
        url = reverse('checkout')
        post_data = {
            'full_name': '',
            'email': 'invalid',
            'phone_number': '123',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'Test City',
            'street_address1': '123 Test St',
            'street_address2': '',
            'county': 'Test County',
            'client_secret': 'pi_test_secret_test',
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("error" in message.tags for message in messages))

class CheckoutSuccessViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.order = Order.objects.create(
            full_name="Test User",
            email="test@example.com",
            phone_number="123456789",
            country="US",
            postcode="12345",
            town_or_city="Test City",
            street_address1="123 Test St",
            street_address2="",
            county="Test County",
            delivery_cost=Decimal("10.00"),
            order_total=Decimal("100.00"),
            grand_total=Decimal("110.00"),
            original_bag='{}',
            stripe_pid='pi_test',
        )
        self.url = reverse('checkout_success', args=[self.order.order_number])

    def test_checkout_success_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertEqual(response.context['order'], self.order)

class WebhookViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('webhook')
        self.signature_header = 't=123,v1=dummy_signature'

    @patch('checkout.webhooks.stripe.Webhook.construct_event')
    def test_webhook_invalid_payload(self, mock_construct_event):
        mock_construct_event.side_effect = ValueError("Invalid payload")
        response = self.client.post(
            self.url, data="{}", content_type='application/json',
            HTTP_STRIPE_SIGNATURE=self.signature_header
        )
        self.assertEqual(response.status_code, 400)

    @patch('checkout.webhooks.stripe.Webhook.construct_event')
    def test_webhook_valid_event(self, mock_construct_event):
        dummy_event = {
            'type': 'payment_intent.succeeded',
            'data': {
                'object': {
                    'id': 'pi_test',
                    'metadata': {
                        'bag': '{}',
                        'save_info': 'on',
                        'username': 'AnonymousUser',
                    },
                    'charges': {
                        'data': [{
                            'billing_details': {'email': 'test@example.com'},
                            'amount': 11000,
                        }]
                    },
                    'shipping': {
                        'phone': '123456789',
                        'address': {
                            'country': 'US',
                            'postal_code': '12345',
                            'city': 'Test City',
                            'line1': '123 Test St',
                            'line2': '',
                            'state': 'Test County',
                        },
                        'name': 'Test User'
                    },
                }
            }
        }
        mock_construct_event.return_value = dummy_event
        with patch('checkout.webhook_handler.StripeWH_Handler.handle_payment_intent_succeeded') as mock_handler:
            mock_handler.return_value = HttpResponse(content="Success", status=200)
            response = self.client.post(
                self.url, data=json.dumps(dummy_event), content_type='application/json',
                HTTP_STRIPE_SIGNATURE=self.signature_header
            )
            self.assertEqual(response.status_code, 200)
            mock_handler.assert_called_once_with(dummy_event)
