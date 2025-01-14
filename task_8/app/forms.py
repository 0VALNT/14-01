from django import forms
from .models import Number, Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = '__all__'
