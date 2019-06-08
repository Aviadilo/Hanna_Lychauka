from django.contrib import admin
from .models import BookInCart, Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'pk', 'books_in_cart_count']

    class Meta:
        model = Cart


admin.site.register(Cart, CartAdmin)
admin.site.register(BookInCart)
