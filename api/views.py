from django.http import JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status

from api.serializers import ServiceSerializer, ClientSerializer, EmployeeSerializer, CoordinatorSerializer
from reservas.models import Service, Client, Employee, Coordinator


# Create your views here.

# API SERVICE
def api_service(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)

    return JsonResponse(serializer.data, safe=False)


def api_service_id(request, service_id):
    service = Service.objects.get(id=service_id)
    serializer = ServiceSerializer(service)

    return JsonResponse(serializer.data, safe=False)


# API CLIENT

def api_client(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)

    return JsonResponse(serializer.data, safe=False)


# API EMPLOYEE
def api_employee(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)

    return JsonResponse(serializer.data, safe=False)


# API COORDINATOR

def api_coordinator(request):
    coordinators = Coordinator.objects.all()
    serializer = CoordinatorSerializer(coordinators, many=True)

    return JsonResponse(serializer.data, safe=False)
