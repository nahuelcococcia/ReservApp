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
    # Obtenemos todos los registros de la tabla Servicios desde la BD
    services = Service.objects.all()
    # Renderizamos el template 'services-list' y como contexto enviamos todos los registros obtenidos
    return render(request, 'services.html', {
        'services': services
    })


def service_register(request):
    form = ServiceForm()  # creamos un formulario acorde al modelo Service, vease forms.py
    if request.method == 'POST':  # Preguntamos si se están enviando los datos del formulario
        # Si se están enviando, entonces crea otro formulario con los datos que se estan enviando
        form = ServiceForm(request.POST)
        if form.is_valid():  # Se valida el formulario
            form.save()  # y Si es válido se guardan los datos del mismo

            return redirect('services-list')     # Y redirigimos a la lista de servicios

    # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el contexto
    #   El formulario acorde al modelo Coordinator
    #   El texto que queremos ponerle al input que enviara los datos
    #   La url hacia donde queremos redirigir si el usuario desea cancelar el registro
    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Registrar Servicio',
        'prev_url': 'services-list'
    })


def service_update(request, service_id):
    service = Service.objects.get(id=service_id)  # Obtenemos el Servicio desde la BD, lo buscamos por id
    if request.method == 'POST':  # Creamos un formulario con los datos  encontrados
        form = ServiceForm(request.POST, instance=service)  # Evaluamos si se están enviando datos
        # Si es asi, creamos un formulario aclarando que se trata de una instancia de un Servicio ya creado
        if form.is_valid():  # Evaluamos si es válido el form
            form.save()  # Si lo es, actualizamos los datos

            return redirect('services-list')  # Y redirigimos a la lista de servicios

    form = ServiceForm(instance=service)

    # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el contexto
    #   El formulario acorde al modelo Coordinator
    #   El texto que queremos ponerle al input que enviara los datos
    #   La url hacia donde queremos redirigir si el usuario desea cancelar el registro
    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Actualizar',
        'prev_url': 'services-list'
    })


def service_activate(request, service_id):
    service = Service.objects.get(id=service_id)    # Obtenemos el Servicio desde la BD, lo buscamos por id
    service.is_active = True     # Se le cambia el atributo is_active a True
    service.save()      # se guardan los cambios

    return redirect("services-list")     # Y redirigimos a la lista de servicios


def service_deactivate(request, service_id):
    service = Service.objects.get(id=service_id)    # Obtenemos el Servicio desde la BD, lo buscamos por id
    service.is_active = False    # Se le cambia el atributo is_active a False
    service.save()   # se guardan los cambios

    return redirect("services-list")     # Y redirigimos a la lista de servicios


def service_delete(request, service_id):
    service = Service.objects.get(id=service_id)    # Obtenemos el Servicio desde la BD, lo buscamos por id
    service.delete()     # Se elimina el registro encontrado

    return redirect("services-list")     # Y redirigimos a la lista de servicios


# RESERVE SERVICE SECTION
def reserves_view(request):
    # Obtenemos  los registros de la tabla Reservas desde la BD, si el empleado,coordinador o servicio no estan activos, no se muestran
    reserves = ReserveService.objects.filter(client__is_active=True).filter(responsible__is_active=True).filter(
        employee__is_active=True).filter(service__is_active=True)
    # Renderizamos el template 'reserves-list' y como contexto enviamos todos los registros obtenidos
    return render(request, 'reserves.html', {
        'reserves': reserves
    })


def reserve_register(request):
    form = ReserveServiceForm() # creamos un formulario acorde al modelo ReserveService, vease forms.py
    if request.method == 'POST':     # Preguntamos si se están enviando los datos del formulario

        form = ReserveServiceForm(request.POST)
        if form.is_valid():       # Se valida el formulario
            form.save()         # y Si es válido se guardan los datos del mismo

            return redirect('reserves-list')     # Y redirigimos a la lista de reservas

    form.fields['client'].queryset = Client.objects.filter(is_active=True)
    form.fields['responsible'].queryset = Coordinator.objects.filter(is_active=True)
    form.fields['employee'].queryset = Employee.objects.filter(is_active=True)
    form.fields['service'].queryset = Service.objects.filter(is_active=True)

    # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el contexto
    #   El formulario acorde al modelo Coordinator
    #   El texto que queremos ponerle al input que enviara los datos
    #   La url hacia donde queremos redirigir si el usuario desea cancelar el registro
    return render(request, 'create_update.html', {
        'form': form,
        "submit": "Registrar Reserva",
        'prev_url': 'reserves-list'
    })


def reserve_update(request, reserve_id):
    reserve = ReserveService.objects.get(id=reserve_id)
    form = ReserveServiceForm(instance=reserve)  # Creamos un formulario con los datos  encontrados
    if request.method == 'POST':         # Preguntamos si se están enviando los datos del formulario
        form = ReserveServiceForm(request.POST, instance=reserve)   # Evaluamos si se están enviando datos
        if form.is_valid():      # Se valida el formulario
            form.save()         # y Si es válido se guardan los datos del mismo

            return redirect('reserves-list')     # Y redirigimos a la lista de reservas

    form.fields['client'].queryset = Client.objects.filter(is_active=True)
    form.fields['responsible'].queryset = Coordinator.objects.filter(is_active=True)
    form.fields['employee'].queryset = Employee.objects.filter(is_active=True)
    form.fields['service'].queryset = Service.objects.filter(is_active=True)

    # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el contexto
    #   El formulario acorde al modelo Coordinator
    #   El texto que queremos ponerle al input que enviara los datos
    #   La url hacia donde queremos redirigir si el usuario desea cancelar el registro
    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Actualizar',
        'prev_url': 'reserves-list'
    })


def reserve_delete(request, reserve_id):
    reserve = ReserveService.objects.get(id=reserve_id)  # Obtenemos la reserva desde la BD, lo buscamos por id
    reserve.delete()    #e eleminamos la reserva

    return redirect('reserves-list')    # Y redirigimos a la lista de reservas
