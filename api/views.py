from django.http import JsonResponse
from django.shortcuts import render

from reservas.models import Service, Client, Employee, Coordinator


# Create your views here.

# API SERVICE
def api_service(request):
    services = Service.objects.all()
    data = services.values()
    list_data = _map_services(data)

    return JsonResponse(list_data, safe=False)


def api_service_id(request, service_id):
    service = Service.objects.get(id=service_id)
    api = _map_service(service)

    return JsonResponse(api, safe=False)


def _map_service(service):
    return {
        'id': service.id,
        'name': service.name,
        'price': service.price
    }


def _map_services(services):
    api_list = []
    for service in services:
        api_list.append({
            'id': service['id'],
            'name': service['price'],
            'price': service['price']
        })
    return api_list


# API CLIENT

def api_client(request):
    clients = Client.objects.all()
    data = clients.values()
    list_data = _map_clients(data)

    return JsonResponse(list_data, safe=False)


def _map_clients(clients):
    api_list = []
    for client in clients:
        api_list.append({
            'id': client['id'],
            'name': client['name'],
            'lastname': client['lastname'],
            'is_active': client['is_active']
        })
    return api_list


# API EMPLOYEE
def api_employee(request):
    employees = Employee.objects.all()
    data = employees.values()
    list_data = _map_employees(data)

    return JsonResponse(list_data, safe=False)


def _map_employees(employees):
    api_list = []
    for employee in employees:
        api_list.append({
            'id': employee['id'],
            'name': employee['name'],
            'lastname': employee['lastname'],
            'file_number': employee['file_number'],
            'is_active': employee['is_active']
        })
    return api_list


# API COORDINATOR

def api_coordinator(request):
    coordinators = Coordinator.objects.all()
    data = coordinators.values()
    list_data = _map_coordinators(data)

    return JsonResponse(list_data, safe=False)


def _map_coordinators(coordinators):
    api_list = []
    for coordinator in coordinators:
        api_list.append({
            'id': coordinator['id'],
            'name': coordinator['name'],
            'lastname': coordinator['lastname'],
            'dni_number': coordinator['dni_number'],
            'created_at': coordinator['created_at'],
            'is_active': coordinator['is_active']
        })
    return api_list
