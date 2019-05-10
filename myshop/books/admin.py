from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'updated_date']  # отображаются указанные поля
    list_filter = ("name", 'author', 'serie', 'genre')  # отфильтровать по полям
    search_fields = [field.name for field in Book._meta.fields]  # поиск по всем полям

    class Meta:
        model = Book


admin.site.register(Book, BookAdmin)
