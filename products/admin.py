from django.contrib import admin
from .models import Product, Category, Wishlist, WishlistItem, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user_profile',
        'created_at',
    )
    ordering = ('-created_at',)


class WishlistItemAdmin(admin.ModelAdmin):
    list_display = (
        'wishlist',
        'product',
        'added_at',
    )
    ordering = ('-added_at',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'product__name', 'content')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(WishlistItem, WishlistItemAdmin)
admin.site.register(Review, ReviewAdmin)
