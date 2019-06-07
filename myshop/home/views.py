from django.shortcuts import render
from django.views.generic.list import ListView
from books.models import Book
from django.db.models import Q
from books.views import book_quantity_in_cart


class LatestView(ListView):
    model = Book
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_quantity_in_cart(self, context)
        return context

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.order_by('-updated_date')[0:3]
