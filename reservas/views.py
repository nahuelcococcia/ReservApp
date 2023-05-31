from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm, CoordinatorForm, ClientForm
from .models import Employee, Coordinator, Client, Service


# Create your views here.
def index(request):
    return HttpResponse("<h1> Hola Mundo </h1>")


def employee_register(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('employee-list')
    
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
    
    return redirect("employee-list")


def employee_update(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            
            return redirect("employee-list")
    form = EmployeeForm(instance=employee)
    
    return render(request, 'employee_update.html', {
        'form': form,
        'submit': 'Actualizar'
    })


def employee_deactivate(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.is_active = False
    employee.save()
    
    return redirect("employee-list")


def employee_delete(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()

    return redirect("employee-list")


# COORDINATOR SECTION
def coordinators_view(request):
    coordinators = Coordinator.objects.all()
    
    return render(request, 'coordinators.html', {
        'coordinators': coordinators
    }) 


def coordinator_register(request):
    form = CoordinatorForm()
    if request.method == 'POST':
        form = CoordinatorForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('coordinators-list')  # Redirect to a success page after registration

    return render(request, 'coordinator_register.html', {
        'form': form,
        "submit": "Registrar Coordinador"
    })

  
def coordinator_update(request, coordinator_id):
    coordinator = Coordinator.objects.get(id=coordinator_id)
    if request.method == 'POST':
        form = CoordinatorForm(request.POST, instance=coordinator)
        if form.is_valid():
            form.save()
            
            return redirect("coordinators-list")
          
    form = CoordinatorForm(instance=coordinator)
    
    return render(request, 'coordinator_update.html', {
        'form': form,
        'submit': 'Actualizar'
    })

  
def coordinator_activate(request, coordinator_id):
    coordinator = Coordinator.objects.get(id=coordinator_id)
    coordinator.is_active = True
    coordinator.save()
    
    return redirect("coordinators-list")


def coordinator_deactivate(request, coordinator_id):
    coordinator = Coordinator.objects.get(id=coordinator_id)
    coordinator.is_active = False
    coordinator.save()
    
    return redirect("coordinators-list")
  
  
def coordinator_delete(request, coordinator_id):
    coordinator = Coordinator.objects.get(id=coordinator_id)
    coordinator.delete()

    return redirect("coordinators-list")


def clients_view(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


def client_update(request, client_id):
    client = Client.objects.get(id=client_id)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            
            return HttpResponse("<p>ya se registro</p>")
    
    
    return render(request, 'client_update.html', {
        'form': form,
        'submit': 'Actualizar'
    })
  

def client_activate(request, client_id):
    client = Client.objects.get(id=client_id)
    client.is_active = True
    client.save()
    return HttpResponse('<h1> Se activo correctamente </h1>')


def client_deactivate(request, client_id):
    client = Client.objects.get(id=client_id)
    client.is_active = False
    client.save()
    return HttpResponse('<h1> Se desactivo correctamente </h1>')


def service_activate(request, service_id):
    service = Service.objects.get(id=service_id)
    service.is_active = True
    service.save()

    return redirect("service-list")


def service_deactivate(request, service_id):
    service = Service.objects.get(id=service_id)
    service.is_active = False
    service.save()

    return redirect("service-list")