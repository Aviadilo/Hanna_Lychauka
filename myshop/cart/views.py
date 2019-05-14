from django.shortcuts import render
from django.views.generic.edit import UpdateView
from cart.models import BookInCart, Cart, User
from books.models import Book
from .forms import AddProductForm
from django.urls import reverse_lazy


class AddProduct(UpdateView):
    model = BookInCart
    form_class = AddProductForm
    template_name = 'cart/cart.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': None})
        else:
            cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': self.request.user})
        self.request.session['cart_id'] = cart.pk
        book_pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=book_pk)
        book_in_cart, created = self.model.objects.get_or_create(cart=cart, book=book, defaults={'quantity': 1})
        if not created:
            book_in_cart.quantity += 1
        return book_in_cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_id'] = self.kwargs.get('pk')
        return context
