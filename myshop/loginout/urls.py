from django.urls import path
from loginout.views import *

urlpatterns = [
    path('login', LoginView.as_view(), name='log-in'),
    path('logout', LogoutView.as_view(), name='log-out'),
]
