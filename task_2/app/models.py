from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    instructions = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

    def get_instructions(self):
        return ", ".join([instruction.name for instruction in self.instructions.all()])