from rest_framework.serializers import ModelSerializer

from reservas.models import Service, Client, Employee, Coordinator


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','name', 'description', 'price']


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','name', 'lastname']


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'lastname', 'file_number']

class CoordinatorSerializer(ModelSerializer):
    class Meta:
        model = Coordinator
        fields = ['id' ,'name', 'lastname', 'dni_number']