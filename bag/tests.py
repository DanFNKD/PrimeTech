from decimal import Decimal
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.conf import settings
from bag.contexts import bag_contents
from bag.views import view_bag, add_to_bag, adjust_bag, remove_from_bag
from products.models import Product

class BagContextsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        # Create a sample product for testing
        self.product = Product.objects.create(
            name="Test Product",
            price=Decimal("50.00"),
        )
        # Prepare a bag with the product (quantity: 2)
        self.session_bag = { str(self.product.pk): 2 }

    def test_bag_contents_context(self):
        # Create a dummy request and assign a session with our bag data
        request = self.factory.get('/')
        request.session = {}  # simulate session dictionary
        request.session['bag'] = self.session_bag
        
        # Call the context processor function
        context = bag_contents(request)
        
        # Expected total: 2 * 50.00 = 100.00
        expected_total = Decimal("100.00")
        self.assertEqual(context['total'], expected_total)
        self.assertEqual(context['product_count'], 2)
        
        # Check delivery calculation based on FREE_DELIVERY_THRESHOLD
        if expected_total < settings.FREE_DELIVERY_THRESHOLD:
            expected_delivery = expected_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
            expected_free_delta = settings.FREE_DELIVERY_THRESHOLD - expected_total
            self.assertEqual(context['delivery'], expected_delivery)
            self.assertEqual(context['free_delivery_delta'], expected_free_delta)
        else:
            self.assertEqual(context['delivery'], 0)
            self.assertEqual(context['free_delivery_delta'], 0)
        
        self.assertEqual(context['grand_total'], context['total'] + context['delivery'])
        self.assertEqual(len(context['bag_items']), 1)
        # Verify that the bag_items list contains our product
        self.assertEqual(context['bag_items'][0]['product'], self.product)


class BagViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name="Test Product",
            price=Decimal("50.00"),
        )
        # Build URLs using Django's reverse lookup
        self.add_url = reverse('add_to_bag', args=[str(self.product.pk)])
        self.adjust_url = reverse('adjust_bag', args=[str(self.product.pk)])
        self.remove_url = reverse('remove_from_bag', args=[str(self.product.pk)])
        self.view_url = reverse('view_bag')

    def test_view_bag(self):
        """Test that the bag view returns status code 200 and uses the correct template."""
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        """Test adding a product to the bag."""
        redirect_url = self.view_url
        post_data = {
            'quantity': '3',
            'redirect_url': redirect_url,
        }
        response = self.client.post(self.add_url, post_data)
        self.assertRedirects(response, redirect_url)
        # Verify that the session now contains the product with quantity 3
        session = self.client.session
        bag = session.get('bag', {})
        self.assertIn(str(self.product.pk), bag)
        self.assertEqual(bag[str(self.product.pk)], 3)

    def test_adjust_bag(self):
        """Test adjusting the quantity in the bag."""
        session = self.client.session
        session['bag'] = { str(self.product.pk): 3 }
        session.save()
        
        # Adjust quantity to 2
        post_data = {
            'quantity': '2'
        }
        response = self.client.post(self.adjust_url, post_data)
        self.assertRedirects(response, reverse('view_bag'))
        session = self.client.session
        bag = session.get('bag', {})
        self.assertIn(str(self.product.pk), bag)
        self.assertEqual(bag[str(self.product.pk)], 2)
        
        # Now adjust quantity to 0 (which should remove the product)
        post_data = {
            'quantity': '0'
        }
        response = self.client.post(self.adjust_url, post_data)
        self.assertRedirects(response, reverse('view_bag'))
        session = self.client.session
        bag = session.get('bag', {})
        self.assertNotIn(str(self.product.pk), bag)

    def test_remove_from_bag(self):
        """Test removing a product from the bag."""
        session = self.client.session
        session['bag'] = { str(self.product.pk): 2 }
        session.save()
        
        response = self.client.post(self.remove_url)
        self.assertEqual(response.status_code, 200)
        session = self.client.session
        bag = session.get('bag', {})
        self.assertNotIn(str(self.product.pk), bag)
