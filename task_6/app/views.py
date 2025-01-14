from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import RecipeForm, CookForm
from .models import Cook, Recipe


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


class CookUpdate(generic.UpdateView):
    model = Cook
    template_name = 'form.html'
    form_class = CookForm
    success_url = reverse_lazy('cook_list')


class RecipeUpdate(generic.UpdateView):
    model = Recipe
    template_name = 'form.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipe_list')


def delete_cook(request, pk):
    obj = Cook.objects.get(pk=pk)
    obj.delete()
    return redirect('cook_list')


def delete_recipe(request, pk):
    obj = Recipe.objects.get(pk=pk)
    obj.delete()
    return redirect('recipe_list')
