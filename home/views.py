import os
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.http import require_POST

# Mailchimp settings from environment
MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')
MAILCHIMP_LIST_ID = os.getenv('MAILCHIMP_LIST_ID')
MAILCHIMP_DC = MAILCHIMP_API_KEY.split('-')[-1] if MAILCHIMP_API_KEY else None  # e.g., 'us7'


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


@require_POST
def subscribe(request):
    """Subscribe user to Mailchimp list"""
    email = request.POST.get('email')

    if not email:
        messages.error(request, "Please enter a valid email.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    # Mailchimp API request
    url = f"https://{MAILCHIMP_DC}.api.mailchimp.com/3.0/lists/{MAILCHIMP_LIST_ID}/members"
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    auth = ('anystring', MAILCHIMP_API_KEY)

    response = requests.post(url, auth=auth, json=data)

    if response.status_code == 200 or response.status_code == 204:
        messages.success(request, "Successfully subscribed to our newsletter!")
    elif response.status_code == 400 and 'already' in response.text:
        messages.info(request, "You are already subscribed.")
    else:
        messages.error(request, "There was an error. Please try again later.")

    return redirect(request.META.get('HTTP_REFERER', '/'))
