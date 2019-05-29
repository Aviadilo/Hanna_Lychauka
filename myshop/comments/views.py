from django.shortcuts import render
from django.views.generic.edit import CreateView
from comments.models import CommentToBook
from comments.forms import CommentCreateForm
from django.urls import reverse_lazy


class CommentCreate(CreateView):
    model = CommentToBook
    template_name = 'books/book_detail.html'
    form_class = CommentCreateForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     checkout_form = CommentCreateForm()
    #     checkout_form.fields['commented_book'].initial = self.object
    #     checkout_form.fields['commented_user'].initial =
    #     context['form'] = checkout_form
    #     return context

    def get_success_url(self):
        return reverse_lazy('book-detail-view', kwargs={'pk': self.kwargs.get('pk')})
