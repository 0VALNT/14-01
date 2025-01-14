from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Record(models.Model):
    name = models.CharField(max_length=256)
    athlete = models.OneToOneField('Athlete', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
