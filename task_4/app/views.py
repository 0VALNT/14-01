from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Order_Item, Order
from .forms import OrderForm, Order_ItemForm


class OrderCreate(generic.CreateView):
    model = Order
    template_name = 'form.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')


class OrderList(generic.ListView):
    model = Order
    template_name = 'list.html'
    context_object_name = 'list'


class OrderDetail(generic.DetailView):
    model = Order
    template_name = 'detail.html'
    context_object_name = 'obj'


class Order_ItemCreate(generic.CreateView):
    model = Order_Item
    template_name = 'form.html'
    form_class = Order_ItemForm
    success_url = reverse_lazy('order_item_list')


class Order_ItemList(generic.ListView):
    model = Order_Item
    template_name = 'list.html'
    context_object_name = 'list'


class Order_ItemDetail(generic.DetailView):
    model = Order_Item
    template_name = 'detail.html'
    context_object_name = 'obj'


class OrderUpdate(generic.UpdateView):
    model = Order
    template_name = 'form.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')


class Order_ItemUpdate(generic.UpdateView):
    model = Order_Item
    template_name = 'form.html'
    form_class = Order_ItemForm
    success_url = reverse_lazy('order_item_list')


def delete_order(request, pk):
    obj = Order.objects.get(pk=pk)
    obj.delete()
    return redirect('order_list')


def delete_order_item(request, pk):
    obj = Order_Item.objects.get(pk=pk)
    obj.delete()
    return redirect('order_item_list')
