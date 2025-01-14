from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)

    def get_authors(self):
        return ", ".join([author.name for author in self.authors.all()])

    def __str__(self):
        return f"{self.title}: {self.get_authors()}"
