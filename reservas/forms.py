import datetime

from django import forms
from django.forms import ModelForm
from .models import Employee, Coordinator, Client, ReserveService, Service


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


class ReserveServiceForm(ModelForm):
    class Meta:
        model = ReserveService
        fields = ['reservation_date', 'client', 'responsible', 'employee', 'service', 'price']
        labels = {
            'reservation_date': 'Fecha Reservación',
            'client': 'Cliente',
            'responsible': 'Responsable',
            'employee': 'Empleado',
            'service': 'Servicio',
            'price': 'Precio',
        }
        widgets = {
            'reservation_date': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'client': forms.Select(attrs={
                'class': 'form-control'
            }),
            'responsible': forms.Select(attrs={
                'class': 'form-control'
            }),
            'employee': forms.Select(attrs={
                'class': 'form-control'
            }),
            'service': forms.Select(attrs={
                'class': 'form-control'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 1
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(is_active=True)
        self.fields['responsible'].queryset = Coordinator.objects.filter(is_active=True)
        self.fields['employee'].queryset = Employee.objects.filter(is_active=True)
        self.fields['service'].queryset = Service.objects.filter(is_active=True)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('reservation_date')
        if date <= datetime.date.today():
            raise forms.ValidationError("La fecha debe ser mayor o igual al dia de hoy")