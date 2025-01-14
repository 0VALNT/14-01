from django import forms
from .models import Record, Athlete


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = '__all__'


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
