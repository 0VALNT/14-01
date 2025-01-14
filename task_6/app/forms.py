from django import forms
from .models import Cook, Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = '__all__'
