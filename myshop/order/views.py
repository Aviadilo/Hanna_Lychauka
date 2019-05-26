from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Order
from .forms import CheckOutOrderForm
from django.urls import reverse_lazy


class OrderCheckOutView(CreateView):
    model = Order
    template_name = 'cart/view-cart.html'
    form_class = CheckOutOrderForm

    def get_success_url(self):
        del self.request.session['cart_id']
        return reverse_lazy('order-success', kwargs={'pk': self.object.pk})


class OrderSuccess(DetailView):
    model = Order
    template_name = 'order/order-success.html'


class OrderList(PermissionRequiredMixin, ListView):
    model = Order
    template_name = 'order/order-list.html'
    permission_required = 'books.edit_order'


class OrderUpdate(PermissionRequiredMixin, UpdateView):
    model = Order
    template_name = 'order/order-update.html'
    fields = ['status']
    permission_required = 'books.edit_order'

    def get_success_url(self):
        return reverse_lazy('order-list')
