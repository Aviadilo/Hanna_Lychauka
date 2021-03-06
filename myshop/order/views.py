from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from .models import Order
from .forms import CheckOutOrderForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from myshop import settings


class OrderCheckOutView(CreateView):
    model = Order
    template_name = 'cart/view-cart.html'
    form_class = CheckOutOrderForm

    def get_success_url(self):
        del self.request.session['cart_id']
        # if self.request.POST.get('email'):
        #     subject = "Заказ"
        #     contact_message = "Заказ получен!"
        #     from_email = settings.EMAIL_HOST_USER
        #     to_email = [self.request.POST.get('email')]
        #     send_mail(
        #         subject,
        #         contact_message,
        #         from_email,
        #         to_email,
        #         fail_silently=False
        #     )
        return reverse_lazy('order-success', kwargs={'pk': self.object.pk})


class OrderSuccess(DetailView):
    model = Order
    template_name = 'order/order-success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_anonymous:
            return context
        if self.request.user.is_authenticated:
            if self.object.cart.user.pk == self.request.user.pk:
                return context


class OrderList(PermissionRequiredMixin, ListView):
    model = Order
    template_name = 'order/order-list.html'
    permission_required = 'books.edit_order'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.order_by('status')


class OrderUpdate(PermissionRequiredMixin, UpdateView):
    model = Order
    template_name = 'order/order-update.html'
    fields = ['status']
    permission_required = 'books.edit_order'

    def get_success_url(self):
        return reverse_lazy('order-list')


class OrderCanceled(UpdateView):
    model = Order
    template_name = 'order/order-canceled.html'
    fields = ['canceled']

    def get_success_url(self):
        self.object.canceled = True
        self.object.save()
        if self.request.user.is_authenticated:
            return reverse_lazy('cart-user-list')
        if self.request.user.is_anonymous:
            return reverse_lazy('book-list-view')
