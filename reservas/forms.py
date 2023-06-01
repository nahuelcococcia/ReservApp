from django import forms
from django.forms import ModelForm
from .models import Employee, Coordinator, Client, Service


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
                "type" : "number",
                'min': '1',
            }),

        }

        
class CoordinatorForm(ModelForm):
    class Meta:
        model = Coordinator
        fields = ['name', 'lastname', 'dni_number']
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'dni_number': 'Numero de Dni',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text'

            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text'
            }),
            'dni_number': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1',
            }),
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'lastname']
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text'

            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text'
            }),
        }


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']
        labels = {
            'name': 'Nombre',
            'Description': 'Descripcion',
            'price': 'Precio'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text'

            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'type': 'text'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 0
            }),
        }