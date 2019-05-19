from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
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
