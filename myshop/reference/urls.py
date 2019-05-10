from django.urls import path
from reference.views import *


urlpatterns = [
    path('all', ReferenceView.as_view(), name='all-references'),

    path('author/<int:pk>', AuthorDetail.as_view(), name='author-detail-view'),
    path('genre/<int:pk>', GenreDetail.as_view(), name='genre-detail-view'),
    path('serie/<int:pk>', SerieDetail.as_view(), name='serie-detail-view'),
    path('publish/<int:pk>', PublishDetail.as_view(), name='publish-detail-view'),
    path('binding/<int:pk>', BindingDetail.as_view(), name='binding-detail-view'),
    path('format/<int:pk>', BookFormatDetail.as_view(), name='format-detail-view'),

    path('author/', AuthorList.as_view(), name='author-list-view'),
    path('genre/', GenreList.as_view(), name='genre-list-view'),
    path('serie/', SerieList.as_view(), name='serie-list-view'),
    path('publish/', PublishList.as_view(), name='publish-list-view'),
    path('binding/', BindingList.as_view(), name='binding-list-view'),
    path('format/', BookFormatList.as_view(), name='format-list-view'),

    path('author-create/', AuthorCreate.as_view(), name='author-create-view'),
    path('genre-create/', GenreCreate.as_view(), name='genre-create-view'),
    path('serie-create/', SerieCreate.as_view(), name='serie-create-view'),
    path('publish-create/', PublishCreate.as_view(), name='publish-create-view'),
    path('binding-create/', BindingCreate.as_view(), name='binding-create-view'),
    path('format-create/', BookFormatCreate.as_view(), name='format-create-view'),

    path('author-update/<int:pk>', AuthorUpdate.as_view(), name='author-update-view'),
    path('genre-update/<int:pk>', GenreUpdate.as_view(), name='genre-update-view'),
    path('serie-update/<int:pk>', SerieUpdate.as_view(), name='serie-update-view'),
    path('publish-update/<int:pk>', PublishUpdate.as_view(), name='publish-update-view'),
    path('binding-update/<int:pk>', BindingUpdate.as_view(), name='binding-update-view'),
    path('format-update/<int:pk>', BookFormatUpdate.as_view(), name='format-update-view'),

    path('author-delete/<int:pk>', AuthorDelete.as_view(), name='author-delete-view'),
    path('genre-delete/<int:pk>', GenreDelete.as_view(), name='genre-delete-view'),
    path('serie-delete/<int:pk>', SerieDelete.as_view(), name='serie-delete-view'),
    path('publish-delete/<int:pk>', PublishDelete.as_view(), name='publish-delete-view'),
    path('binding-delete/<int:pk>', BindingDelete.as_view(), name='binding-delete-view'),
    path('format-delete/<int:pk>', BookFormatDelete.as_view(), name='format-delete-view'),
]
