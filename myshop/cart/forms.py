from django import forms
from django.forms import ModelForm
from .models import *


class AddBookForm(ModelForm):
    class Meta:
        model = BookInCart
        fields = ['cart', 'book', 'quantity']
        widgets = {'book': forms.HiddenInput} # не показывать поле book в форме
