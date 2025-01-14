from django import forms
from .models import Order_Item, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class Order_ItemForm(forms.ModelForm):
    class Meta:
        model = Order_Item
        fields = '__all__'
