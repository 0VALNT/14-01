from django.db import models


class Number(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=256)
    number = models.OneToOneField('Number', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
