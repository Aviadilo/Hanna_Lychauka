from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DeleteView
from .models import Book
from django.urls import reverse_lazy
from .forms import BookForm


class BookList(ListView):
    model = Book
    template_name = 'books/book_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('name', 0)
        if qs.filter(name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs


class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreate(CreateView):
    model = Book
    template_name = 'books/create_form.html'
    form_class = BookForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('book-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('book-list-view')
        return reverse_lazy('book-create-view')


class BookUpdate(UpdateView):
    model = Book
    template_name = 'books/update_form.html'
    form_class = BookForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('book-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('book-list-view')


class BookDelete(DeleteView):
    model = Book
    template_name = 'books/delete_form.html'

    def get_success_url(self):
        return reverse_lazy('book-list-view')
