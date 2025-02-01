from django.test import TestCase
from django.urls import reverse
from .models import FAQ

class FAQModelTest(TestCase):
    def test_str_method(self):
        faq = FAQ.objects.create(
            question="What is your return policy?",
            answer="Our return policy is 30 days with receipt."
        )
        self.assertEqual(str(faq), "What is your return policy?")

class FAQViewTest(TestCase):
    def setUp(self):
        FAQ.objects.create(
            question="What is FAQ?",
            answer="FAQ stands for frequently asked questions."
        )
        FAQ.objects.create(
            question="How can I contact support?",
            answer="You can contact support via email."
        )

    def test_faq_view_status_code(self):
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)

    def test_faq_view_template_used(self):
        response = self.client.get(reverse('faq'))
        self.assertTemplateUsed(response, 'faq/faq.html')

    def test_faq_view_context(self):
        response = self.client.get(reverse('faq'))
        self.assertIn('faqs', response.context)
        self.assertEqual(len(response.context['faqs']), 2)
