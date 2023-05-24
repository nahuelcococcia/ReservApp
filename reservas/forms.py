from django import forms
from django.forms import ModelForm
from .models import Employee, Coordinator


class EmployeeForm(ModelForm):
       class Meta:
        model = Employee
        fields = ['name', 'lastname', 'file_number' ]
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'file_number': 'Numero de Legajo',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'file_number': forms.TextInput(attrs={
                'class': 'form-control',
                "type" : "number"
            }),

        }


class CoordinatorForm(ModelForm):
    class Meta:
        model = Coordinator
        fields = ['name', 'lastname', 'dni_number', 'created_at', 'is_active']
        labels = {
            'name': "Nombre",
            'lastname': "Apellido",
            'dni_number': "Nro. DNI",
            'is_active': "Activo"
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'dni_number': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            })
        }