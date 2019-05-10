from django import forms
from django.forms import ModelForm
from .models import *


class SearchForm(forms.Form):
    name = forms.CharField(label="Поиск по названию")


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'country']


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class SerieForm(ModelForm):
    class Meta:
        model = Series
        fields = ['name', 'description']


class PublishForm(ModelForm):
    class Meta:
        model = Publish
        fields = ['name', 'country', 'city']

class BindingForm(ModelForm):
    class Meta:
        model = Binding
        fields = ['binding_type']


class BookFormatForm(ModelForm):
    class Meta:
        model = BookFormat
        fields = ['size']
