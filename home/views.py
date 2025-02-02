from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

from django.http import HttpResponse

def robots_txt(request):
    content = """User-agent: *
Disallow: /admin/
Disallow: /checkout/
Disallow: /cart/
Disallow: /profile/
Allow: /products/
Allow: /faq/
Allow: /blog/
Sitemap: https://yourdomain.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")

