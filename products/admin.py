from django.contrib import admin
from .models import Product, Category, Wishlist, WishlistItem


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'get_category',
        'price',
        'rating',
        'image',
    )
    ordering = ('sku',)

    def get_category(self, obj):
        """
        Returns the product's category's friendly_name or name.
        If there's no category, returns 'No category'.
        """
        if obj.category:
            return obj.category.friendly_name or obj.category.name
        return "No category"

    # The label shown in the admin list header
    get_category.short_description = 'Category'


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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(WishlistItem, WishlistItemAdmin)
