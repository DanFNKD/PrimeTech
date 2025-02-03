from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def about(request):
    """ A view to return the about page """
    return render(request, 'about.html')

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
Sitemap: https://primetechfnkd-382d679752d9.herokuapp.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")

def custom_404(request, exception):
    """ Custom 404 error page """
    return render(request, '404.html', status=404)
