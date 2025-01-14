from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import School, Director
from .forms import DirectorForm, SchoolForm


class DirectorCreate(generic.CreateView):
    model = Director
    template_name = 'form.html'
    form_class = DirectorForm
    success_url = reverse_lazy('director_list')


class DirectorList(generic.ListView):
    model = Director
    template_name = 'list.html'
    context_object_name = 'list'


class DirectorDetail(generic.DetailView):
    model = Director
    template_name = 'detail.html'
    context_object_name = 'obj'


def director_delete(request, pk):
    director = Director.objects.get(pk=pk)
    director.delete()
    return redirect('director_list')


class SchoolCreate(generic.CreateView):
    model = School
    template_name = 'form.html'
    form_class = SchoolForm
    success_url = reverse_lazy('school_list')


class SchoolList(generic.ListView):
    model = School
    template_name = 'list.html'
    context_object_name = 'list'


class SchoolDetail(generic.DetailView):
    model = School
    template_name = 'detail.html'
    context_object_name = 'obj'


def school_delete(request, pk):
    school = School.objects.get(pk=pk)
    school.delete()
    return redirect('school_list')


class SchoolUpdate(generic.UpdateView):
    model = School
    template_name = 'form.html'
    form_class = SchoolForm
    success_url = reverse_lazy('school_list')


class DirectorUpdate(generic.UpdateView):
    model = Director
    template_name = 'form.html'
    form_class = DirectorForm
    success_url = reverse_lazy('director_list')
