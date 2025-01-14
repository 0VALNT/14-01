from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_attendee(self):
        return ", ".join([attendee.name for attendee in Book.objects.filter(library_id=self.id)])


class Book(models.Model):
    name = models.CharField(max_length=256)
    library = models.ForeignKey('Library', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
