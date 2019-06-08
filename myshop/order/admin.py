from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['cart', 'status', 'canceled', 'created_day']

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)
