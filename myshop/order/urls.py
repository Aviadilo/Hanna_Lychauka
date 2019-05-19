from django.urls import path
from order.views import *

urlpatterns = [
    path('order-create', OrderCheckOutView.as_view(), name='order-create'),
    path('order-success/<int:pk>', OrderSuccess.as_view(), name='order-success')
]
