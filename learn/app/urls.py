from django.urls import path, include
from .views import BookList, BookDetailView, BookCreateView, BookDeleteView, BookUpdateView
from .views import AuthorList, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView
from .views import GenreList, GenreDetailView, GenreCreateView, GenreUpdateView, GenreDeleteView
urlpatterns = [
    path('book/list/', BookList.as_view(), name='book_list'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/list/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),

    path('author/list/', AuthorList.as_view(), name='author_list'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('author/list/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('author/update/<int:pk>', AuthorUpdateView.as_view(), name='author_update'),
    path('author/delete/<int:pk>', AuthorDeleteView.as_view(), name='author_delete'),

    path('genre/list/', GenreList.as_view(), name='genre_list'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genre/list/<int:pk>', GenreDetailView.as_view(), name='genre_detail'),
    path('genre/update/<int:pk>', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<int:pk>', GenreDeleteView.as_view(), name='genre_delete'),
]
