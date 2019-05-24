from django.shortcuts import render
from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    template_name = 'loginout/login.html'


class LogoutView(auth_views.LogoutView):
    extra_context = 'none'
