from django.urls import path
from books.views import *

urlpatterns = [
    path('all', BookList.as_view(), name='book-list-view'),
    path('book/<int:pk>', BookDetail.as_view(), name='book-detail-view'),
    path('book-create/', BookCreate.as_view(), name='book-create-view'),
    path('book-update/<int:pk>', BookUpdate.as_view(), name='book-update-view'),
    path('book-delete/<int:pk>', BookDelete.as_view(), name='book-delete-view'),
    path('book-search/', BookSearch.as_view(), name='book-search-view'),
]
