from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Ingredient, Recipe
from .forms import RecipeForm, IngredientForm


class RecipeCreate(generic.CreateView):
    model = Recipe
    template_name = 'form.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipe_list')


class RecipeList(generic.ListView):
    model = Recipe
    template_name = 'list.html'
    context_object_name = 'list'


class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'detail.html'
    context_object_name = 'obj'


class IngredientCreate(generic.CreateView):
    model = Ingredient
    template_name = 'form.html'
    form_class = IngredientForm
    success_url = reverse_lazy('ingredient_list')


class IngredientList(generic.ListView):
    model = Ingredient
    template_name = 'list.html'
    context_object_name = 'list'


class IngredientDetail(generic.DetailView):
    model = Ingredient
    template_name = 'detail.html'
    context_object_name = 'obj'
