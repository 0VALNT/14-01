from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Cook, Recipe
from .forms import RecipeForm, CookForm


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


class CookCreate(generic.CreateView):
    model = Cook
    template_name = 'form.html'
    form_class = CookForm
    success_url = reverse_lazy('cook_list')


class CookList(generic.ListView):
    model = Cook
    template_name = 'list.html'
    context_object_name = 'list'


class CookDetail(generic.DetailView):
    model = Cook
    template_name = 'detail.html'
    context_object_name = 'obj'
