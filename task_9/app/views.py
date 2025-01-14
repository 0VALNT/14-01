from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Record, Athlete
from .forms import AthleteForm, RecordForm


class AthleteCreate(generic.CreateView):
    model = Athlete
    template_name = 'form.html'
    form_class = AthleteForm
    success_url = reverse_lazy('athlete_list')


class AthleteList(generic.ListView):
    model = Athlete
    template_name = 'list.html'
    context_object_name = 'list'


class AthleteDetail(generic.DetailView):
    model = Athlete
    template_name = 'detail.html'
    context_object_name = 'obj'


def athlete_delete(request, pk):
    athlete = Athlete.objects.get(pk=pk)
    athlete.delete()
    return redirect('athlete_list')


class RecordCreate(generic.CreateView):
    model = Record
    template_name = 'form.html'
    form_class = RecordForm
    success_url = reverse_lazy('record_list')


class RecordList(generic.ListView):
    model = Record
    template_name = 'list.html'
    context_object_name = 'list'


class RecordDetail(generic.DetailView):
    model = Record
    template_name = 'detail.html'
    context_object_name = 'obj'


def record_delete(request, pk):
    record = Record.objects.get(pk=pk)
    record.delete()
    return redirect('record_list')


class RecordUpdate(generic.UpdateView):
    model = Record
    template_name = 'form.html'
    form_class = RecordForm
    success_url = reverse_lazy('record_list')


class AthleteUpdate(generic.UpdateView):
    model = Athlete
    template_name = 'form.html'
    form_class = AthleteForm
    success_url = reverse_lazy('athlete_list')
