# from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *


def get_cancel_url(self, context):
    context['cancel_url'] = self.get_success_url()
    return context


class ReferenceView(TemplateView):
    template_name = 'reference/references.html'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'reference/detail/author_detail.html'


class GenreDetail(DetailView):
    model = Genre
    template_name = 'reference/detail/genre_detail.html'


class SerieDetail(DetailView):
    model = Series
    template_name = 'reference/detail/series_detail.html'


class PublishDetail(DetailView):
    model = Publish
    template_name = 'reference/detail/publish_detail.html'


class BindingDetail(DetailView):
    model = Binding
    template_name = 'reference/detail/binding_detail.html'


class BookFormatDetail(DetailView):
    model = BookFormat
    template_name = 'reference/detail/bookformat_detail.html'


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


class AuthorCreate(CreateView):
    model = Author
    template_name = 'reference/form/create_form.html'
    form_class = AuthorForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('author-list-view')
        return reverse_lazy('author-create-view')


class GenreCreate(CreateView):
    model = Genre
    template_name = 'reference/form/create_form.html'
    form_class = GenreForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('genre-list-view')
        return reverse_lazy('genre-create-view')


class SerieCreate(CreateView):
    model = Series
    template_name = 'reference/form/create_form.html'
    form_class = SerieForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('serie-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('serie-list-view')
        return reverse_lazy('serie-create-view')


class PublishCreate(CreateView):
    model = Publish
    template_name = 'reference/form/create_form.html'
    form_class = PublishForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publish-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('publish-list-view')
        return reverse_lazy('publish-create-view')


class BindingCreate(CreateView):
    model = Binding
    template_name = 'reference/form/create_form.html'
    form_class = BindingForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('binding-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('binding-list-view')
        return reverse_lazy('binding-create-view')


class BookFormatCreate(CreateView):
    model = BookFormat
    template_name = 'reference/form/create_form.html'
    form_class = BookFormatForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('format-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('format-list-view')
        return reverse_lazy('format-create-view')


class AuthorUpdate(UpdateView):
    model = Author
    template_name = 'reference/form/update_form.html'
    form_class = AuthorForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('author-list-view')


class GenreUpdate(UpdateView):
    model = Genre
    template_name = 'reference/form/update_form.html'
    form_class = GenreForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('genre-list-view')


class SerieUpdate(UpdateView):
    model = Series
    template_name = 'reference/form/update_form.html'
    form_class = SerieForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('serie-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('serie-list-view')


class PublishUpdate(UpdateView):
    model = Publish
    template_name = 'reference/form/update_form.html'
    form_class = PublishForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publish-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('publish-list-view')


class BindingUpdate(UpdateView):
    model = Binding
    template_name = 'reference/form/update_form.html'
    form_class = BindingForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('binding-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('binding-list-view')


class BookFormatUpdate(UpdateView):
    model = BookFormat
    template_name = 'reference/form/update_form.html'
    form_class = BookFormatForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('format-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('format-list-view')


class AuthorDelete(DeleteView):
    model = Author
    template_name = 'reference/form/delete_form.html'

    def get_success_url(self):
        return reverse_lazy('author-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class GenreDelete(DeleteView):
    model = Genre
    template_name = 'reference/form/delete_form.html'

    def get_success_url(self):
        return reverse_lazy('genre-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class SerieDelete(DeleteView):
    model = Series
    template_name = 'reference/form/delete_form.html'

    def get_success_url(self):
        return reverse_lazy('serie-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class PublishDelete(DeleteView):
    model = Publish
    template_name = 'reference/form/delete_form.html'

    def get_success_url(self):
        return reverse_lazy('publish-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class BindingDelete(DeleteView):
    model = Binding
    template_name = 'reference/form/delete_form.html'

    def get_success_url(self):
        return reverse_lazy('binding-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class BookFormatDelete(DeleteView):
    model = BookFormat
    template_name = 'reference/form/delete_form.html'

    def get_success_url(self):
        return reverse_lazy('format-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)
