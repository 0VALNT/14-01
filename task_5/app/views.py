from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Book, Library
from .forms import LibraryForm, BookForm


class LibraryCreate(generic.CreateView):
    model = Library
    template_name = 'form.html'
    form_class = LibraryForm
    success_url = reverse_lazy('library_list')


class LibraryList(generic.ListView):
    model = Library
    template_name = 'list.html'
    context_object_name = 'list'


class LibraryDetail(generic.DetailView):
    model = Library
    template_name = 'detail.html'
    context_object_name = 'obj'


class BookCreate(generic.CreateView):
    model = Book
    template_name = 'form.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')


class BookList(generic.ListView):
    model = Book
    template_name = 'list.html'
    context_object_name = 'list'


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'obj'
    
class BookUpdate(generic.UpdateView):
    model = Book
    template_name = 'form.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')


class LibraryUpdate(generic.UpdateView):
    model = Library
    template_name = 'form.html'
    form_class = LibraryForm
    success_url = reverse_lazy('library_list')


def delete_book(request, pk):
    obj = Book.objects.get(pk=pk)
    obj.delete()
    return redirect('book_list')


def delete_library(request, pk):
    obj = Library.objects.get(pk=pk)
    obj.delete()
    return redirect('library_list')
