from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, UpdateView
from cart.models import User
from django.urls import reverse_lazy
from .forms import CreateUserForm


class LoginView(auth_views.LoginView):
    template_name = 'loginout/login.html'


class LogoutView(auth_views.LogoutView):
    extra_context = 'none'


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'loginout/password_templates/password_reset_form.html'
    email_template_name = 'loginout/password_templates/password_reset_email.html'
    subject_template_name = 'loginout/password_templates/password_reset_subject.txt'
    success_url = '/'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'loginout/password_templates/password_reset_confirm.html'
    success_url = '/'


class CreateUser(CreateView):
    model = User
    template_name = 'loginout/registration/create_user.html'
    form_class = CreateUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        self.object.set_password(self.object.password)
        self.object.save()
        return self.request.POST.get('next', '/')
