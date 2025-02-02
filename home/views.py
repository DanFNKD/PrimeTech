from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def create_admin_user(request):
    """ Temporary view to create a superuser """
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "AdminPassword123")
        return HttpResponse("Superuser created successfully!")
    return HttpResponse("Superuser already exists.")
