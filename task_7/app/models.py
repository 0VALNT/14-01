from django.db import models


class School(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=256)
    school = models.OneToOneField('School', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
