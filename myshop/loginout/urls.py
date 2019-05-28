from django.urls import path
from loginout.views import *

urlpatterns = [
    path('login', LoginView.as_view(), name='log-in'),
    path('logout', LogoutView.as_view(), name='log-out'),
    # path('password-reset', PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset-done', PasswordResetView.as_view(), name='password_reset'),
    # path('password-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #      PasswordResetView.as_view(), name='password_reset_confirm'),
    path('create-user', CreateUser.as_view(), name='create-user'),
]
