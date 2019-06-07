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
from comments.forms import CommentCreateForm
from django.db.models import Q


def book_quantity_in_cart(self, context):
    cart_id = self.request.session.get('cart_id', '0')
    if cart_id != '0':
        context['quantity'] = Cart.objects.get(pk=cart_id).books_in_cart_count
    else:
        context['quantity'] = cart_id
    return context

class BookList(ListView):
    model = Book
    template_name = 'books/book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/books/all'
        book_quantity_in_cart(self, context)
        return context

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('search_book', 0)
        if qs.filter(Q(name__icontains=search) | Q(author__first_name__icontains=search)).distinct().exists():
            return qs.filter(Q(name__icontains=search) | Q(author__first_name__icontains=search)).distinct()
        return qs


class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/books/book/{}'.format(self.object.pk)
        checkout_form = CommentCreateForm()
        checkout_form.fields['commented_book'].initial = self.object
        checkout_form.fields['commented_user'].initial = self.request.user
        context['form'] = checkout_form
        book_quantity_in_cart(self, context)
        return context


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'books/create_form.html'
    form_class = BookForm
    permission_required = 'books.edit_content'

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
    permission_required = 'books.edit_content'

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
    permission_required = 'books.edit_content'

    def get_success_url(self):
        return reverse_lazy('book-list-view')
