from django import forms
from django.forms import ModelForm
from .models import *


class CommentCreateForm(ModelForm):
    class Meta:
        model = CommentToBook
        fields = ['commented_book', 'comment_to_book', 'commented_user']
        widgets = {'commented_book': forms.HiddenInput, 'commented_user': forms.HiddenInput}
