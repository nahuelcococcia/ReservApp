from django.shortcuts import render, redirect
from .forms import EmployeeForm, CoordinatorForm, ClientForm, ServiceForm, ReserveServiceForm
from .models import Employee, Coordinator, Client, Service, ReserveService


# view para la HomePage de ReservApp, donde solo se renderiza el template 'index.html'
def index(request):
    return render(request, 'index.html')


def handler404(request, exception):
    return render(request, '404.html', {
        'title': 'Pagina no encontrada',
        'msg': 'No se encontro la pagina solicitada, verífque que la url es correcta',
        'url_prev': 'home'
    })

# EMPLOYEE SECTION
# View para listar los Empleados
def employees_view(request):
    # Obtenemos todos los Empleados de la BD
    employees = Employee.objects.all()

    # Renderizamos el template 'employees.html' y como contexto enviamos todos los empleados obtenidos
    return render(request, 'employees.html', {
        'employees': employees
    })


# View para registrar un nuevo Empleado
def employee_register(request):
    form = EmployeeForm()  # creamos un formulario acorde al modelo Coordinator, vease forms.py
    if request.method == 'POST':  # Preguntamos si se están enviando los datos del formulario
        # Si se están enviando, entonces crea otro formulario con dichos datos
        form = EmployeeForm(request.POST)
        if form.is_valid():  # Se valida el formulario
            form.save()  # y Si es válido se guardan los datos del mismo

            return redirect('employee-list')  # Por ultimo redirige hacia el listado de Empleados

    # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el contexto
    #   El formulario acorde al modelo Employee
    #   El texto que queremos ponerle al input que enviara los datos
    #   La url hacia donde queremos redirigir si el usuario desea cancelar el registro
    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Registrar Empleado',
        'prev_url': 'employee-list'
    })


# View para Actualizar Empleado existente
def employee_update(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)  # Obtenemos el Empleado desde la BD, lo buscamos por id
        form = EmployeeForm(instance=employee)  # Creamos un formulario con los datos del Empleado encontrado

        if request.method == 'POST':  # Evaluamos si se están enviando datos
            # Si es asi, creamos un formulario aclarando que se trata de una instancia de un Empleado ya creado
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():  # Evaluamos si es válido el form
                form.save()

                return redirect('employee-list')  # Por ultimo redirige hacia el listado de Empleados

        # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el
        # contexto El formulario acorde al modelo Employee El texto que queremos ponerle al input que enviara los
        # datos La url hacia donde queremos redirigir si el usuario desea cancelar la actualizacion
        return render(request, 'create_update.html', {
            'form': form,
            'submit': 'Actualizar Empleado',
            'prev_url': 'employee-list'
        })
    except Employee.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Actualizar',
            'msg': 'No se encontró Empleado con el id proporcionado',
            'url_prev': 'employee-list'
        })


# View para activar un Empleado, dada una id válida
def employee_activate(request, id):
    try:
        employee = Employee.objects.get(id=id)  # Se busca el Empleado en la BD por id
        employee.is_active = True  # Se le cambia el atributo is_active a True
        employee.save()  # se guardan los cambios

        return redirect("employee-list")  # Por ultimo redirige hacia el listado de Empleados
    except Employee.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Activar',
            'msg': 'No se encontró Empleado con el id proporcionado',
            'url_prev': 'employee-list'
        })


# View para desactivar un Empleado, dada una id válida
def employee_deactivate(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)  # Se busca el Empleado en la BD por id
        employee.is_active = False  # Se le cambia el atributo is_active a False
        employee.save()  # se guardan los cambios

        return redirect("employee-list")  # Por ultimo redirige hacia el listado de Empleados
    except Employee.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Desactivar',
            'msg': 'No se encontró Empleado con el id proporcionado',
            'url_prev': 'employee-list'
        })


# View para eliminar un Empleado, dada una id válida
def employee_delete(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)  # Se busca el Empleado en la BD por id
        employee.delete()  # se elimina dicho Empleado

        return redirect("employee-list")  # Por ultimo redirige hacia el listado de Empleados
    except Employee.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Eliminar',
            'msg': 'No se encontró Empleado con el id proporcionado',
            'url_prev': 'employee-list'
        })


# COORDINATOR SECTION
# View para listar los Coordinadores
def coordinators_view(request):
    # Obtenemos todos los registros de la tabla Coordinator desde la BD
    coordinators = Coordinator.objects.all()

    # Renderizamos el template 'coordinators.html' y como contexto enviamos todos los registros obtenidos
    return render(request, 'coordinators.html', {
        'coordinators': coordinators
    })

    # En el template se creará una tabla, teniendo como columnas a los atributos que nos interesan mostrar y como
    # filas a los registros que se cargaron


# View para registrar un nuevo Coordinador
def coordinator_register(request):
    form = CoordinatorForm()  # creamos un formulario acorde al modelo Coordinator, vease forms.py
    if request.method == 'POST':  # Preguntamos si se están enviando los datos del formulario
        # Si se están enviando, entonces crea otro formulario con los datos que se estan enviando
        form = CoordinatorForm(request.POST)
        if form.is_valid():  # Se valida el formulario
            form.save()  # y Si es válido se guardan los datos del mismo

            return redirect('coordinators-list')  # Por ultimo redirige hacia el listado de Coordinadores

    # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el contexto
    #   El formulario acorde al modelo Coordinator
    #   El texto que queremos ponerle al input que enviara los datos
    #   La url hacia donde queremos redirigir si el usuario desea cancelar el registro
    return render(request, 'create_update.html', {
        'form': form,
        "submit": "Registrar Coordinador",
        'prev_url': 'coordinators-list'
    })


# View para actualizar un Coordinador registrado, dada una id válida
def coordinator_update(request, coordinator_id):
    try:
        coordinator = Coordinator.objects.get(id=coordinator_id)  # Obtenemos el Coordinador desde la BD, lo buscamos por id
        form = CoordinatorForm(instance=coordinator)  # Creamos un formulario con los datos del Coordinador encontrado

        if request.method == 'POST':  # Evaluamos si se están enviando datos
            # Si es asi, creamos un formulario aclarando que se trata de una instancia de un Coordinator ya creado
            form = CoordinatorForm(request.POST, instance=coordinator)
            if form.is_valid():  # Evaluamos si es válido el form
                form.save()  # Si lo es, actualizamos los datos

                return redirect("coordinators-list")  # Y redirigimos a la lista de Coordinadores

        # Si no se enviaron datos entonces se renderiza el template 'create_update.html' incluyendo en el contexto:
        #   El formulario cargado
        #   El texto que deseamos mostrar en el input que envía los datos, en este caso 'Actualizar'
        #   y la URL a donde queremos redirigir por si el usuario cancela la actualización
        return render(request, 'create_update.html', {
            'form': form,
            'submit': 'Actualizar Coordinador',
            'prev_url': 'coordinators-list'
        })
    except Coordinator.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Actualizar',
            'msg': 'No se encontró Coordinador con el id proporcionado',
            'url_prev': 'coordinators-list'
        })


# View para activar un Coordinador, dada una id válida
def coordinator_activate(request, coordinator_id):
    try:
        coordinator = Coordinator.objects.get(id=coordinator_id)  # Se busca el Coordinador en la BD
        coordinator.is_active = True  # Se le cambia el atributo is_active a True
        coordinator.save()  # se guardan los cambios

        return redirect("coordinators-list")  # Por ultimo se redirige hacia el listado de Coordinadores
    except Coordinator.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Activar',
            'msg': 'No se encontró Coordinador con el id proporcionado',
            'url_prev': 'coordinators-list'
        })


# View para desactivar un Coordinador, dada una id válida
def coordinator_deactivate(request, coordinator_id):
    try:
        coordinator = Coordinator.objects.get(id=coordinator_id)  # Se busca el Coordinador en la BD
        coordinator.is_active = False  # Se le cambia el atributo is_active a False
        coordinator.save()  # se guardan los cambios

        return redirect("coordinators-list")  # Por ultimo se redirige hacia el listado de Coordinadores
    except Coordinator.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Desactivar',
            'msg': 'No se encontró Coordinador con el id proporcionado',
            'url_prev': 'coordinators-list'
        })


# View para eliminar un Coordinador, dada una id válida
def coordinator_delete(request, coordinator_id):
    try:
        coordinator = Coordinator.objects.get(id=coordinator_id)  # Se busca el Coordinador en la BD
        coordinator.delete()  # Se elimina el registro encontrado

        return redirect("coordinators-list")  # Por ultimo se redirige hacia el listado de Coordinadores
    except Coordinator.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Eliminar',
            'msg': 'No se encontró Coordinador con el id proporcionado',
            'url_prev': 'coordinators-list'
        })


# CLIENT SECTION   
# view para listar los Clientes almacenados
def clients_view(request):
    clients = Client.objects.all()  # Obtenemos todos los Clientes desde la BD
    # Renderizamos el template 'clients.html' y como contexto enviamos todos los clientes obtenidos
    return render(request, 'clients.html', {
        'clients': clients
    })


# view para registrar un nuevo Cliente
def client_register(request):
    form = ClientForm()  # creamos un formulario acorde al modelo Client, vease forms.py
    if request.method == 'POST':  # Preguntamos si se están enviando los datos del formulario
        # Si se están enviando, entonces crea otro formulario con dichos datos
        form = ClientForm(request.POST)
        if form.is_valid():  # Se valida el formulario
            form.save()  # y si es válido se guardan los datos del mismo

            return redirect('clients-list')  # Por ultimo redirige hacia el listado de Clientes

    # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el contexto
    #   El formulario acorde al modelo Client
    #   El texto que queremos ponerle al input que enviara los datos
    #   La url hacia donde queremos redirigir si el usuario desea cancelar el registro      
    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Registrar Cliente',
        'prev_url': 'clients-list'
    })


# view para actualizar un Cliente existente
def client_update(request, client_id):
    try:
        client = Client.objects.get(id=client_id)  # Obtenemos el Cliente desde la BD, lo buscamos por id
        form = ClientForm(instance=client)  # Creamos un formulario con los datos del Cliente encontrado

        if request.method == 'POST':  # Evaluamos si se están enviando datos
            # Si es asi, creamos un formulario aclarando que se trata de una instancia de un Cliente ya creado
            form = ClientForm(request.POST, instance=client)
            if form.is_valid():  # Evaluamos si es válido el form
                form.save()  # y si es válido actualizamos los datos

                return redirect("clients-list")  # Por ultimo redirige hacia el listado de Clientes

        # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el contexto
        #   El formulario acorde al modelo Client
        #   El texto que queremos ponerle al input que enviara los datos
        #   La url hacia donde queremos redirigir si el usuario desea cancelar la actualizacion
        return render(request, 'create_update.html', {
            'form': form,
            'submit': 'Actualizar Cliente',
            'prev_url': 'clients-list'
        })
    except Client.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Actualizar',
            'msg': 'No se encontró Cliente con el id proporcionado',
            'url_prev': 'clients-list'
        })


# View para activar un Cliente, dada una id válida
def client_activate(request, client_id):
    try:
        client = Client.objects.get(id=client_id)  # Se busca el Cliente en la BD, por id
        client.is_active = True  # Se modifica el atributo is_active a True
        client.save()  # Se elimina el registro encontrado

        return redirect("clients-list")  # Por ultimo redirige hacia el listado de Clientes
    except Client.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Activar',
            'msg': 'No se encontró Cliente con el id proporcionado',
            'url_prev': 'clients-list'
        })


# View para desactivar un Cliente, dada una id válida
def client_deactivate(request, client_id):
    try:
        client = Client.objects.get(id=client_id)  # Se busca el Cliente en la BD, por id
        client.is_active = False  # Se modifica el atributo is_active a False
        client.save()  # Se elimina el registro encontrado

        return redirect("clients-list")  # Por ultimo redirige hacia el listado de Clientes
    except Client.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Desactivar',
            'msg': 'No se encontró Cliente con el id proporcionado',
            'url_prev': 'clients-list'
        })


# View para eliminar un Cliente, dada una id válida
def client_delete(request, client_id):
    try:
        client = Client.objects.get(id=client_id)  # Se busca el Cliente en la BD, por id
        client.delete()

        return redirect("clients-list")  # Por ultimo redirige hacia el listado de Clientes
    except Client.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Eliminar',
            'msg': 'No se encontró Cliente con el id proporcionado',
            'url_prev': 'clients-list'
        })


# SERVICE SECTION
# view para listar los Servicios almacenados
def service_view(request):
    # Obtenemos todos los registros de la tabla Servicios desde la BD
    services = Service.objects.all()
    # Renderizamos el template 'services.html' y como contexto enviamos todos los registros obtenidos
    return render(request, 'services.html', {
        'services': services
    })


# view para registrar un nuevo Servicio
def service_register(request):
    form = ServiceForm()  # creamos un formulario acorde al modelo Service, vease forms.py
    if request.method == 'POST':  # Preguntamos si se están enviando los datos del formulario
        # Si se están enviando, entonces crea otro formulario con los datos que se estan enviando
        form = ServiceForm(request.POST)
        if form.is_valid():  # Se valida el formulario
            form.save()  # y Si es válido se guardan los datos del mismo

            return redirect('services-list')  # Y redirigimos a la lista de servicios

    # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el contexto
    #   El formulario acorde al modelo Service
    #   El texto que queremos ponerle al input que enviara los datos
    #   La url hacia donde queremos redirigir si el usuario desea cancelar el registro
    return render(request, 'create_update.html', {
        'form': form,
        'submit': 'Registrar Servicio',
        'prev_url': 'services-list'
    })


# view para actualizar Servicio existente
def service_update(request, service_id):
    try:
        service = Service.objects.get(id=service_id)  # Obtenemos el Servicio desde la BD, lo buscamos por id
        if request.method == 'POST':  # Creamos un formulario con los datos  encontrados
            form = ServiceForm(request.POST, instance=service)  # Evaluamos si se están enviando datos
            # Si es asi, creamos un formulario aclarando que se trata de una instancia de un Servicio ya creado
            if form.is_valid():  # Evaluamos si es válido el form
                form.save()  # Si lo es, actualizamos los datos

                return redirect('services-list')  # Y redirigimos a la lista de servicios

        form = ServiceForm(instance=service)

        # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el contexto
        #   El formulario acorde al modelo Service
        #   El texto que queremos ponerle al input que enviara los datos
        #   La url hacia donde queremos redirigir si el usuario desea cancelar el registro
        return render(request, 'create_update.html', {
            'form': form,
            'submit': 'Actualizar Servicio',
            'prev_url': 'services-list'
        })
    except Service.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Actualizar',
            'msg': 'No se encontró Servicio con el id proporcionado',
            'url_prev': 'services-list'
        })


# view para activar Servicio existente
def service_activate(request, service_id):
    try:
        service = Service.objects.get(id=service_id)  # Obtenemos el Servicio desde la BD, lo buscamos por id
        service.is_active = True  # Se le cambia el atributo is_active a True
        service.save()  # se guardan los cambios

        return redirect("services-list")  # Y redirigimos a la lista de servicios
    except Client.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Activar',
            'msg': 'No se encontró Servicio con el id proporcionado',
            'url_prev': 'services-list'
        })


# view para desactivar Servicio existente
def service_deactivate(request, service_id):
    try:
        service = Service.objects.get(id=service_id)  # Obtenemos el Servicio desde la BD, lo buscamos por id
        service.is_active = False  # Se le cambia el atributo is_active a False
        service.save()  # se guardan los cambios

        return redirect("services-list")  # Y redirigimos a la lista de servicios
    except Client.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Desactivar',
            'msg': 'No se encontró Servicio con el id proporcionado',
            'url_prev': 'services-list'
        })


# view para eliminar Servicio existente
def service_delete(request, service_id):
    try:
        service = Service.objects.get(id=service_id)  # Obtenemos el Servicio desde la BD, lo buscamos por id
        service.delete()  # Se elimina el registro encontrado

        return redirect("services-list")  # Y redirigimos a la lista de servicios
    except Client.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Eliminar',
            'msg': 'No se encontró Servicio con el id proporcionado',
            'url_prev': 'services-list'
        })


# RESERVE SERVICE SECTION
# view para listar las Reservas almacenadas
def reserves_view(request):
    # Obtenemos  los registros de la tabla Reservas desde la BD, si el empleado,coordinador o servicio no estan
    # activos, no se muestran
    reserves = ReserveService.objects.filter(client__is_active=True).filter(responsible__is_active=True).filter(
        employee__is_active=True).filter(service__is_active=True)
    # Renderizamos el template 'reserves.html' y como contexto enviamos todos los registros obtenidos

    return render(request, 'reserves.html', {
        'reserves': reserves
    })


# view para registrar un nueva Reserva
def reserve_register(request):
    form = ReserveServiceForm()  # creamos un formulario acorde al modelo ReserveService, vease forms.py
    if request.method == 'POST':  # Preguntamos si se están enviando los datos del formulario

        form = ReserveServiceForm(request.POST)
        if form.is_valid():  # Se valida el formulario
            form.save()  # y Si es válido se guardan los datos del mismo

            return redirect('reserves-list')  # Y redirigimos a la lista de reservas
    # Se filtran los Clientes, Coordinadores, Empleados y Servicios que esten activos para incluirlos como opcion en el widget corresp
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


# view para actualizar una Reserva existente
def reserve_update(request, reserve_id):
    try:
        reserve = ReserveService.objects.get(id=reserve_id)
        form = ReserveServiceForm(instance=reserve)  # Creamos un formulario con los datos  encontrados
        if request.method == 'POST':  # Preguntamos si se están enviando los datos del formulario
            form = ReserveServiceForm(request.POST, instance=reserve)  # Evaluamos si se están enviando datos
            if form.is_valid():  # Se valida el formulario
                form.save()  # y Si es válido se guardan los datos del mismo

                return redirect('reserves-list')  # Y redirigimos a la lista de reservas
        # Se filtran los Clientes, Coordinadores, Empleados y Servicios que esten activos para incluirlos como opcion
        # en el widget corresp
        form.fields['client'].queryset = Client.objects.filter(is_active=True)
        form.fields['responsible'].queryset = Coordinator.objects.filter(is_active=True)
        form.fields['employee'].queryset = Employee.objects.filter(is_active=True)
        form.fields['service'].queryset = Service.objects.filter(is_active=True)

        # Si aun no se están enviando datos entonces renderiza el template 'create-update.html' incluyendo en el
        # contexto El formulario acorde al modelo Coordinator El texto que queremos ponerle al input que enviara los
        # datos La url hacia donde queremos redirigir si el usuario desea cancelar el registro
        return render(request, 'create_update.html', {
            'form': form,
            'submit': 'Actualizar Reserva',
            'prev_url': 'reserves-list'
        })
    except ReserveService.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Actualizar',
            'msg': 'No se encontróReserva con el id proporcionado',
            'url_prev': 'reserves-list'
        })


# view para eliminar una Reserva existente
def reserve_delete(request, reserve_id):
    try:
        reserve = ReserveService.objects.get(id=reserve_id)  # Obtenemos la reserva desde la BD, lo buscamos por id
        reserve.delete()  # e eleminamos la reserva

        return redirect('reserves-list')  # Y redirigimos a la lista de reservas
    except Client.DoesNotExist:
        return render(request, 'error_message.html', {
            'title': 'Error al Eliminar',
            'msg': 'No se encontró Reserva con el id proporcionado',
            'url_prev': 'reserves-list'
        })