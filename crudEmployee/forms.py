from django import forms
from .models import crudEmployee


class EmpForms(forms.ModelForm):
    class Meta:
        model = crudEmployee
        fields = '__all__'
