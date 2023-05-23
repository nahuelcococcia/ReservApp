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
  
  
def employee_update(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            # Por ahora solo muestra un mensaje pero lo mejor seria que lleve al listado
            return HttpResponse('<h1> Empleado actualizado </h1>')

    form = EmployeeForm(instance=employee)
    return render(request, 'create_update_form.html', {
        'form': form,
        'submit': 'Actualizar'
    })

  
def employee_deactivate(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.is_active = False
    employee.save()
    return HttpResponse('<h1> Se desactivo con exito </h1>')
