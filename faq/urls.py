from django.urls import path
from .views import faq_view, FAQDetailView

urlpatterns = [
    path('', faq_view, name='faq'),
    path('<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
]
