from django.http import JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status

from api.serializers import ServiceSerializer, ClientSerializer, EmployeeSerializer, CoordinatorSerializer
from reservas.models import Service, Client, Employee, Coordinator


# Create your views here.

# API SERVICE
@api_view(['GET'])
def api_service(request):
    try:
        services = Service.objects.all()

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def api_service_id(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


# API CLIENT

def api_client(request):
    clients = Client.objects.all()
    try:
        serializer = ClientSerializer(clients, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

# API EMPLOYEE
def api_employee(request):
    try:
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


# API COORDINATOR

def api_coordinator(request):
    try:
        coordinators = Coordinator.objects.all()
        serializer = CoordinatorSerializer(coordinators, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
