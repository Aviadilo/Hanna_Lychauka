from django.urls import path
from home.views import LatestView

from . import views

urlpatterns = [
    path('', LatestView.as_view(), name='latest-list-view')
]
