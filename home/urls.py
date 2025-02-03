from django.urls import path
from .views import index, about, robots_txt, custom_404

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('robots.txt', robots_txt, name='robots_txt'),
]
