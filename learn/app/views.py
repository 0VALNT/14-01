from django.shortcuts import render
from .models import Book, Author, Genre
from django.views import generic
from .forms import BookForm, GenreForm, AuthorForm
from django.urls import reverse_lazy


class BookList(generic.ListView):
    model = Book
    template_name = 'list.html'
    context_object_name = 'list'


class AuthorList(generic.ListView):
    model = Author
    template_name = 'list.html'
    context_object_name = 'list'


class GenreList(generic.ListView):
    model = Genre
    template_name = 'list.html'
    context_object_name = 'list'


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'obj'
    template_name = 'detail.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'obj'
    template_name = 'detail.html'


class GenreDetailView(generic.DetailView):
    model = Genre
    context_object_name = 'obj'
    template_name = 'detail.html'


class BookDeleteView(generic.DetailView):
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'form.html'
    template_name_suffix = ''


class AuthorDeleteView(generic.DetailView):
    model = Author
    success_url = reverse_lazy('author_list')
    template_name = 'form.html'


class GenreDeleteView(generic.DetailView):
    model = Genre
    success_url = reverse_lazy('genre_list')
    template_name = 'form.html'


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'form.html'
    success_url = reverse_lazy('book_list')
    form_class = BookForm


class AuthorCreateView(generic.CreateView):
    model = Author
    template_name = 'form.html'
    success_url = reverse_lazy('author_list')
    form_class = AuthorForm


class GenreCreateView(generic.CreateView):
    model = Genre
    template_name = 'form.html'
    success_url = reverse_lazy('genre_list')
    form_class = GenreForm


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'form.html'
    success_url = reverse_lazy('book_list')
    form_class = BookForm


class GenreUpdateView(generic.UpdateView):
    model = Genre
    template_name = 'form.html'
    success_url = reverse_lazy('genre_list')
    form_class = GenreForm


class AuthorUpdateView(generic.UpdateView):
    model = Author
    template_name = 'form.html'
    success_url = reverse_lazy('author_list')
    form_class = AuthorForm
