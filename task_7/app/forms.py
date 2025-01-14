from django import forms
from .models import School, Director


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
