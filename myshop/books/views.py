from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Book
from cart.models import Cart
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', '0')
        if cart_id != '0':
            context['quantity'] = Cart.objects.get(pk=cart_id).books_in_cart_count
        else:
            context['quantity'] = cart_id
        context['logout_redirect'] = '/books/all'
        return context


class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_pk = self.kwargs.get('pk')
        context['logout_redirect'] = '/books/book/{}'.format(book_pk)
        return context


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'books/create_form.html'
    form_class = BookForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('book-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('book-list-view')
        return reverse_lazy('book-create-view')


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'books/update_form.html'
    form_class = BookForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('book-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('book-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/delete_form.html'
    permission_required = 'books.edit-content'

    def get_success_url(self):
        return reverse_lazy('book-list-view')
