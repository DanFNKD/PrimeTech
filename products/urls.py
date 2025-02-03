# products/urls.py

from django.urls import path
from .views import (
    all_products, product_detail, add_product, edit_product,
    delete_product, add_to_wishlist, remove_from_wishlist, view_wishlist,
    submit_review, delete_review
)

urlpatterns = [
    path('', all_products, name='products'),
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist,
    name='add_to_wishlist'),
    path('wishlist/remove/<int:item_id>/', remove_from_wishlist,
    name='remove_from_wishlist'),
    path('wishlist/', view_wishlist, name='view_wishlist'),
    path('<int:product_id>/review/', submit_review, name='submit_review'),
    path('review/delete/<int:review_id>/', delete_review, name='delete_review'),
]
