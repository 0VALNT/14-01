from django.db import models


class Cook(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_attendee(self):
        return ", ".join([attendee.name for attendee in Recipe.objects.filter(cook_id=self.id)])


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    cook = models.ForeignKey('cook', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
