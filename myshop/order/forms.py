from django import forms
from django.forms import ModelForm
from .models import *


class CheckOutOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['cart', 'status', 'delivery_address', 'email', 'phone']
        widgets = {'cart': forms.HiddenInput, 'status': forms.HiddenInput} # не показывать поля cart и status в форме
