
from django.shortcuts import render
from django.views.generic.list import ListView
from books.models import Book
from django.db.models import Q


class LatestView(ListView):
    model = Book
    template_name = 'home/home.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('name', 0)
        if search != 0:
            return qs.filter(Q(name__icontains=search) | Q(author__first_name__icontains=search)).distinct()
        return qs.order_by('-updated_date')[0:3]
