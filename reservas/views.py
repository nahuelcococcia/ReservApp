from django.shortcuts import render, redirect
from .forms import EmployeeForm, CoordinatorForm, ClientForm, ServiceForm, ReserveServiceForm
from .models import Employee, Coordinator, Client, Service, ReserveService


# Create your views here.
def index(request):
    return render(request, 'index.html')


# EMPLOYEE SECTION
def employees_view(request):
    employees = Employee.objects.all()

    return render(request, 'employees.html', {
        'employees': employees
    })


def employee_register(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('employee-list')
    
    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Registrar Empleado',
        'prev_url': 'employee-list'
    })


def employee_update(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            
            return redirect('employee-list')

    form = EmployeeForm(instance=employee)
    
    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Actualizar',
        'prev_url': 'employee-list'
    })


def employee_activate(request, id):
    employee = Employee.objects.get(id=id)
    employee.is_active = True
    employee.save()

    return redirect("employee-list")


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

    return render(request, 'create_update.html', {
        'form': form,
        "submit": "Registrar Coordinador",
        'prev_url': 'coordinators-list'
    })

  
def coordinator_update(request, coordinator_id):
    coordinator = Coordinator.objects.get(id=coordinator_id)
    if request.method == 'POST':
        form = CoordinatorForm(request.POST, instance=coordinator)
        if form.is_valid():
            form.save()
            
            return redirect("coordinators-list")
          
    form = CoordinatorForm(instance=coordinator)
    
    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Actualizar',
        'prev_url': 'coordinators-list'
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

    return render(request, 'clients.html', {
        'clients': clients
    })


def client_register(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('clients-list')

    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Registrar Cliente',
        'prev_url': 'clients-list'
    })


def client_update(request, client_id):
    client = Client.objects.get(id=client_id)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            
            return redirect("clients-list")

    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Actualizar',
        'prev_url': 'clients-list'
    })
  

def client_activate(request, client_id):
    client = Client.objects.get(id=client_id)
    client.is_active = True
    client.save()

    return redirect("clients-list")


def client_deactivate(request, client_id):
    client = Client.objects.get(id=client_id)
    client.is_active = False
    client.save()

    return redirect("clients-list")


def client_delete(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()

    return redirect("clients-list")


# SERVICE SECTION
def service_view(request):
    services = Service.objects.all()

    return render(request, 'services.html', {
        'services': services
    })


def service_register(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('services-list')

    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Registrar Servicio',
        'prev_url': 'services-list'
    })


def service_update(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()

            return redirect('services-list')

    form = ServiceForm(instance=service)

    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Actualizar',
        'prev_url': 'services-list'
    })


def service_activate(request, service_id):
    service = Service.objects.get(id=service_id)
    service.is_active = True
    service.save()

    return redirect("services-list")


def service_deactivate(request, service_id):
    service = Service.objects.get(id=service_id)
    service.is_active = False
    service.save()
    
    return redirect("services-list")


def service_delete(request, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()

    return redirect("services-list")
  
  
# RESERVE SERVICE SECTION
def reserves_view(request):
    reserves = ReserveService.objects.filter(client__is_active=True).filter(responsible__is_active=True).filter(employee__is_active=True).filter(service__is_active=True)

    return render(request, 'reserves.html', {
        'reserves': reserves
    })


def reserve_register(request):
    form = ReserveServiceForm()
    if request.method == 'POST':
        form = ReserveServiceForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('reserves-list')

    form.fields['client'].queryset = Client.objects.filter(is_active=True)
    form.fields['responsible'].queryset = Coordinator.objects.filter(is_active=True)
    form.fields['employee'].queryset = Employee.objects.filter(is_active=True)
    form.fields['service'].queryset = Service.objects.filter(is_active=True)

    return render(request, 'create_update.html', {
        'form': form,
        "submit": "Registrar Reserva",
        'prev_url': 'reserves-list'
    })


def reserve_update(request, reserve_id):
    reserve = ReserveService.objects.get(id=reserve_id)
    form = ReserveServiceForm(instance=reserve)
    if request.method == 'POST':
        form = ReserveServiceForm(request.POST, instance=reserve)
        if form.is_valid():
            form.save()

            return redirect('reserves-list')

    form.fields['client'].queryset = Client.objects.filter(is_active=True)
    form.fields['responsible'].queryset = Coordinator.objects.filter(is_active=True)
    form.fields['employee'].queryset = Employee.objects.filter(is_active=True)
    form.fields['service'].queryset = Service.objects.filter(is_active=True)

    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Actualizar',
        'prev_url': 'reserves-list'
    })


def reserve_delete(request, reserve_id):
    reserve = ReserveService.objects.get(id=reserve_id)
    reserve.delete()

    return redirect('reserves-list')

