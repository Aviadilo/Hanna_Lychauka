from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['first_name']
    search_fields = ['last_name', 'first_name']
    ordering = ['first_name']

    class Meta:
        model = Author

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Series)
admin.site.register(Publish)
admin.site.register(Binding)
admin.site.register(OrderStatus)
