from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def index(request):
    return HttpResponse("<h1> Hola Mundo </h1>")

def employee_register(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            return redirect('home')  # Redirect to a success page after registration
    form = EmployeeForm()
    return render(request, 'employee_register.html', {
        'form': form,
         "submit": "Registrar Empleado"
         })


def employee_desactivate(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.is_active = False
    return HttpResponse('<h1> Se desactivo con exito </h1>')