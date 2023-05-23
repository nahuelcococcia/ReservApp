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
            form.save()
            return redirect('home')  # Redirect to a success page after registration
    form = EmployeeForm()
    return render(request, 'employee_register.html', {
        'form': form,
        "submit": "Registrar Empleado"
    })


def employees_view(request):
    employees = Employee.objects.all()

    return render(request, 'employees.html', {'employees': employees})


def employee_activate(request, id):
    employee = Employee.objects.get(id=id)
    employee.is_active = True
    employee.save()
    message = "El empleado ha sido activado correctamente."

    return render(request, 'employee_activate.html', {'message': message})