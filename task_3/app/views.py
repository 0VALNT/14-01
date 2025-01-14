from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Attendee, Event
from .forms import EventForm, AttendeeForm


class EventCreate(generic.CreateView):
    model = Event
    template_name = 'form.html'
    form_class = EventForm
    success_url = reverse_lazy('event_list')


class EventList(generic.ListView):
    model = Event
    template_name = 'list.html'
    context_object_name = 'list'


class EventDetail(generic.DetailView):
    model = Event
    template_name = 'detail.html'
    context_object_name = 'obj'


class AttendeeCreate(generic.CreateView):
    model = Attendee
    template_name = 'form.html'
    form_class = AttendeeForm
    success_url = reverse_lazy('attendee_list')


class AttendeeList(generic.ListView):
    model = Attendee
    template_name = 'list.html'
    context_object_name = 'list'


class AttendeeDetail(generic.DetailView):
    model = Attendee
    template_name = 'detail.html'
    context_object_name = 'obj'


class AttendeeUpdate(generic.UpdateView):
    model = Attendee
    template_name = 'form.html'
    form_class = AttendeeForm
    success_url = reverse_lazy('attendee_list')


class EventUpdate(generic.UpdateView):
    model = Event
    template_name = 'form.html'
    form_class = EventForm
    success_url = reverse_lazy('event_list')


def delete_attendee(request, pk):
    obj = Attendee.objects.get(pk=pk)
    obj.delete()
    return redirect('attendee_list')


def delete_event(request, pk):
    obj = Event.objects.get(pk=pk)
    obj.delete()
    return redirect('event_list')
