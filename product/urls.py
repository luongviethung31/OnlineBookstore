from django.urls import path

from .views import (
    ListAuthor,
    ListGenre,
    ListBook,
    RetrieveBook,
    RetrieveGenre,
    RetrieveAuthor,
    CreateBook
)

urlpatterns = [
    path('genres/', ListGenre.as_view(), name='genres'),
    path('books/', ListBook.as_view(), name='books'),
    path('authors/', ListAuthor.as_view(), name='authors'),
    path('book/<str:slug>/', RetrieveBook.as_view(), name='retrieve-book'),
    path('genre/<str:slug>/', RetrieveGenre.as_view(), name='retrieve-genre'),
    path('author/<str:slug>/', RetrieveAuthor.as_view(), name='retrieve-author'),
    path('create-book/', CreateBook.as_view(), name='create=book')

]
 