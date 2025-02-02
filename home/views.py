from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def robots_txt(request):
    """ A view to return the robots.txt file """
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

def custom_404(request, exception):
    """ Custom 404 error page """
    return render(request, '404.html', status=404)
