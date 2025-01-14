from django import forms
from .models import Book, Library


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
