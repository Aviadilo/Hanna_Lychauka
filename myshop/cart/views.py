from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from cart.models import BookInCart, Cart, User
from books.models import Book
from .forms import AddBookForm
from reference.models import OrderStatus
from order.forms import CheckOutOrderForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

new_order_status = OrderStatus.objects.get(pk=1)  # у объекта с pk=1 лежит значение "Новый заказ"


class AddBookToCart(UpdateView):
    model = BookInCart
    form_class = AddBookForm
    template_name = 'cart/add-book.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            user = None
            # если класть в 'user' не пустоту, а объект класса User:
            # user_anon = User(username='Anonymous', is_staff = False, is_superuser = False)
            # user_anon.save()
            # cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user_anon})
        else:
            user = self.request.user
        cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        self.request.session['cart_id'] = cart.pk
        book_pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=book_pk)
        book_in_cart, created = self.model.objects.get_or_create(cart=cart, book=book, defaults={'quantity': 1})
        if not created:
            book_in_cart.quantity += 1
        return book_in_cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        if self.request.POST.get('back'):
            product = self.model.objects.get(pk=self.object.pk)
            if product.quantity > 1:
                product.quantity -= 1
                product.save()
            else:
                product.delete()
        return self.request.POST.get('next', '/')


class CartView(DetailView):
    model = Cart
    template_name = 'cart/view-cart.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user
        cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        checkout_form = CheckOutOrderForm()
        checkout_form.fields['cart'].initial = self.object
        checkout_form.fields['status'].initial = new_order_status
        context['form'] = checkout_form
        return context


class DeleteBookFromCart(DeleteView):
    model = BookInCart
    template_name = 'cart/delete-book.html'

    def get_success_url(self):
        return reverse_lazy('view-cart')
