from django.urls import path
from order.views import *

urlpatterns = [
    path('order-create', OrderCheckOutView.as_view(), name='order-create'),
    path('order-success/<int:pk>', OrderSuccess.as_view(), name='order-success'),
    path('order-list', OrderList.as_view(), name='order-list'),
    path('order-update/<int:pk>', OrderUpdate.as_view(), name='order-update'),
    path('order-canceled/<int:pk>', OrderCanceled.as_view(), name='order-canceled'),
]
