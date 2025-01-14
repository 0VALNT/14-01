from django.shortcuts import render, redirect
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


class RecipeUpdate(generic.UpdateView):
    model = Recipe
    template_name = 'form.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipe_list')


class IngredientUpdate(generic.UpdateView):
    model = Ingredient
    template_name = 'form.html'
    form_class = IngredientForm
    success_url = reverse_lazy('ingredient_list')


def delete_recipe(request, pk):
    obj = Recipe.objects.get(pk=pk)
    obj.delete()
    return redirect('recipe_list')


def delete_ingredient(request, pk):
    obj = Ingredient.objects.get(pk=pk)
    obj.delete()
    return redirect('ingredient_list')
