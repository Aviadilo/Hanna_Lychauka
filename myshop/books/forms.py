from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name',
                  'author',
                  'image',
                  'price',
                  'serie',
                  'genre',
                  'year',
                  'page',
                  'bind',
                  'book_format',
                  'isbn',
                  'weight',
                  'age_limit',
                  'publish',
                  'book_amount',
                  'available',
                  'rate']
