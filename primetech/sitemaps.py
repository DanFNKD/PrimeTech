from django.contrib.sitemaps import Sitemap
from products.models import Product
from faq.models import FAQ


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_on

    def location(self, obj):
        return obj.get_absolute_url()


class FAQSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return FAQ.objects.all()

    def lastmod(self, obj):
        return obj.updated_on

    def location(self, obj):
        return obj.get_absolute_url()
