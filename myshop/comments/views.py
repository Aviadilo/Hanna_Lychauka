from django.shortcuts import render
from django.views.generic.edit import CreateView
from comments.models import CommentToBook
from comments.forms import CommentCreateForm
from django.urls import reverse_lazy


class CommentCreate(CreateView):
    model = CommentToBook
    template_name = 'books/book_detail.html'
    form_class = CommentCreateForm

    def get_success_url(self):
        return reverse_lazy('book-detail-view', kwargs={'pk': self.object.commented_book.pk})
