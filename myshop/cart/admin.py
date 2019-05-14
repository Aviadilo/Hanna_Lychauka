from django.contrib import admin
from .models import BookInCart, Cart

admin.site.register(Cart)
admin.site.register(BookInCart)
