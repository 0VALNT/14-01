from django.db import models


class Attendee(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=256)
    attendees = models.ManyToManyField(Attendee)
    date = models.DateField()

    def __str__(self):
        return self.name

    def get_attendee(self):
        return ", ".join([attendee.name for attendee in self.attendees.all()])
