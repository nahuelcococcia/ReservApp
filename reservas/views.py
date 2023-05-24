from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee, Coordinator

# Create your views here.
def index(request):
    return HttpResponse("<h1> Hola Mundo </h1>")


def employee_register(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')  # Redirect to a success page after registration
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
    return redirect("list")
  
  
def employee_update(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            # Por ahora solo muestra un mensaje pero lo mejor seria que lleve al listado
            return redirect("list")

    form = EmployeeForm(instance=employee)
    return render(request, 'employee_update.html', {
        'form': form,
        'submit': 'Actualizar'
    })

  
def employee_deactivate(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.is_active = False
    employee.save()
    return redirect("list")


def employee_delete(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()

    return redirect("list")


def coordinators_view(request):
    coordinators = Coordinator.objects.all()
    return render(request, 'employees.html', {'coordinators': coordinators})