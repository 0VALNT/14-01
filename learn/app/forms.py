from .models import Book, Genre, Author
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
