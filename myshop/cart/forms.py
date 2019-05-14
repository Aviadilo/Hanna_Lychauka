from django import forms
from django.forms import ModelForm
from .models import *


class AddProductForm(ModelForm):
    class Meta:
        model = BookInCart
        fields = ['cart', 'book', 'quantity']
