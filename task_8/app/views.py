from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Number, Device
from .forms import DeviceForm, NumberForm


class DeviceCreate(generic.CreateView):
    model = Device
    template_name = 'form.html'
    form_class = DeviceForm
    success_url = reverse_lazy('device_list')


class DeviceList(generic.ListView):
    model = Device
    template_name = 'list.html'
    context_object_name = 'list'


class DeviceDetail(generic.DetailView):
    model = Device
    template_name = 'detail.html'
    context_object_name = 'obj'


def device_delete(request, pk):
    device = Device.objects.get(pk=pk)
    device.delete()
    return redirect('device_list')


class NumberCreate(generic.CreateView):
    model = Number
    template_name = 'form.html'
    form_class = NumberForm
    success_url = reverse_lazy('number_list')


class NumberList(generic.ListView):
    model = Number
    template_name = 'list.html'
    context_object_name = 'list'


class NumberDetail(generic.DetailView):
    model = Number
    template_name = 'detail.html'
    context_object_name = 'obj'

def number_delete(request, pk):
    number = Number.objects.get(pk=pk)
    number.delete()
    return redirect('number_list')