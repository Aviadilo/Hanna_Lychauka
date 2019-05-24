# from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .forms import *
from .models import *


def get_cancel_url(self, context):
    context['cancel_url'] = self.get_success_url()
    return context


class ReferenceView(TemplateView):
    template_name = 'reference/references.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/refs/all'
        return context


class AuthorDetail(DetailView):
    model = Author
    template_name = 'reference/detail/author_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'author-update-view'
        context['delete_url'] = 'author-delete-view'
        author_pk = self.kwargs.get('pk')
        context['logout_redirect'] = '/refs/author/{}'.format(author_pk)
        return context


class GenreDetail(DetailView):
    model = Genre
    template_name = 'reference/detail/genre_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'genre-update-view'
        context['delete_url'] = 'genre-delete-view'
        genre_pk = self.kwargs.get('pk')
        context['logout_redirect'] = '/refs/genre/{}'.format(genre_pk)
        return context


class SerieDetail(DetailView):
    model = Series
    template_name = 'reference/detail/series_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'serie-update-view'
        context['delete_url'] = 'serie-delete-view'
        serie_pk = self.kwargs.get('pk')
        context['logout_redirect'] = '/refs/serie/{}'.format(serie_pk)
        return context



class PublishDetail(DetailView):
    model = Publish
    template_name = 'reference/detail/publish_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'publish-update-view'
        context['delete_url'] = 'publish-delete-view'
        publish_pk = self.kwargs.get('pk')
        context['logout_redirect'] = '/refs/publish/{}'.format(publish_pk)
        return context


class BindingDetail(DetailView):
    model = Binding
    template_name = 'reference/detail/binding_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'binding-update-view'
        context['delete_url'] = 'binding-delete-view'
        binding_pk = self.kwargs.get('pk')
        context['logout_redirect'] = '/refs/binding/{}'.format(binding_pk)
        return context


class BookFormatDetail(DetailView):
    model = BookFormat
    template_name = 'reference/detail/bookformat_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'format-update-view'
        context['delete_url'] = 'format-delete-view'
        format_pk = self.kwargs.get('pk')
        context['logout_redirect'] = '/refs/format/{}'.format(format_pk)
        return context


class AuthorList(ListView):
    model = Author
    template_name = 'reference/list/author_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('name', 0)
        if qs.filter(first_name__icontains=search).exists():
            return qs.filter(first_name__icontains=search)
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/refs/author'
        return context


class GenreList(ListView):
    model = Genre
    template_name = 'reference/list/genre_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('name', 0)
        if qs.filter(name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/refs/genre'
        return context

    # def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context['search_name'] = SearchForm()
    #         search = self.request.GET.get('name', 0)
    #         if context['object_list'].filter(name__icontains=search).exists():
    #             context['object_list'] = context['object_list'].filter(name__icontains=search)
    #             return context
    #         else:
    #             return context


class SerieList(ListView):
    model = Series
    template_name = 'reference/list/series_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('name', 0)
        if qs.filter(name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/refs/serie'
        return context


class PublishList(ListView):
    model = Publish
    template_name = 'reference/list/publish_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('name', 0)
        if qs.filter(name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/refs/publish'
        return context


class BindingList(ListView):
    model = Binding
    template_name = 'reference/list/binding_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('name', 0)
        if qs.filter(binding_type__icontains=search).exists():
            return qs.filter(binding_type__icontains=search)
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/refs/binding'
        return context


class BookFormatList(ListView):
    model = BookFormat
    template_name = 'reference/list/bookformat_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('name', 0)
        if qs.filter(size__icontains=search).exists():
            return qs.filter(size__icontains=search)
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/refs/format'
        return context


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    template_name = 'reference/form/create_form.html'
    form_class = AuthorForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('author-list-view')
        return reverse_lazy('author-create-view')


class GenreCreate(PermissionRequiredMixin, CreateView):
    model = Genre
    template_name = 'reference/form/create_form.html'
    form_class = GenreForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('genre-list-view')
        return reverse_lazy('genre-create-view')


class SerieCreate(PermissionRequiredMixin, CreateView):
    model = Series
    template_name = 'reference/form/create_form.html'
    form_class = SerieForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('serie-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('serie-list-view')
        return reverse_lazy('serie-create-view')


class PublishCreate(PermissionRequiredMixin, CreateView):
    model = Publish
    template_name = 'reference/form/create_form.html'
    form_class = PublishForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publish-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('publish-list-view')
        return reverse_lazy('publish-create-view')


class BindingCreate(PermissionRequiredMixin, CreateView):
    model = Binding
    template_name = 'reference/form/create_form.html'
    form_class = BindingForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('binding-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('binding-list-view')
        return reverse_lazy('binding-create-view')


class BookFormatCreate(PermissionRequiredMixin, CreateView):
    model = BookFormat
    template_name = 'reference/form/create_form.html'
    form_class = BookFormatForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('format-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('format-list-view')
        return reverse_lazy('format-create-view')


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    template_name = 'reference/form/update_form.html'
    form_class = AuthorForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('author-list-view')


class GenreUpdate(PermissionRequiredMixin, UpdateView):
    model = Genre
    template_name = 'reference/form/update_form.html'
    form_class = GenreForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('genre-list-view')


class SerieUpdate(PermissionRequiredMixin, UpdateView):
    model = Series
    template_name = 'reference/form/update_form.html'
    form_class = SerieForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('serie-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('serie-list-view')


class PublishUpdate(PermissionRequiredMixin, UpdateView):
    model = Publish
    template_name = 'reference/form/update_form.html'
    form_class = PublishForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publish-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('publish-list-view')


class BindingUpdate(PermissionRequiredMixin, UpdateView):
    model = Binding
    template_name = 'reference/form/update_form.html'
    form_class = BindingForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('binding-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('binding-list-view')


class BookFormatUpdate(PermissionRequiredMixin, UpdateView):
    model = BookFormat
    template_name = 'reference/form/update_form.html'
    form_class = BookFormatForm
    permission_required = 'books.edit-content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('format-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('format-list-view')


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    template_name = 'reference/form/delete_form.html'
    permission_required = 'books.edit-content'

    def get_success_url(self):
        return reverse_lazy('author-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class GenreDelete(PermissionRequiredMixin, DeleteView):
    model = Genre
    template_name = 'reference/form/delete_form.html'
    permission_required = 'books.edit-content'

    def get_success_url(self):
        return reverse_lazy('genre-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class SerieDelete(PermissionRequiredMixin, DeleteView):
    model = Series
    template_name = 'reference/form/delete_form.html'
    permission_required = 'books.edit-content'

    def get_success_url(self):
        return reverse_lazy('serie-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class PublishDelete(PermissionRequiredMixin, DeleteView):
    model = Publish
    template_name = 'reference/form/delete_form.html'
    permission_required = 'books.edit-content'

    def get_success_url(self):
        return reverse_lazy('publish-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class BindingDelete(PermissionRequiredMixin, DeleteView):
    model = Binding
    template_name = 'reference/form/delete_form.html'
    permission_required = 'books.edit-content'

    def get_success_url(self):
        return reverse_lazy('binding-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class BookFormatDelete(PermissionRequiredMixin, DeleteView):
    model = BookFormat
    template_name = 'reference/form/delete_form.html'
    permission_required = 'books.edit-content'

    def get_success_url(self):
        return reverse_lazy('format-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)
