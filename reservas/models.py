from django.db import models
from datetime import  datetime


# Create your models here.
class Modelo1(models.Model):
    campo1 = models.CharField(max_length=50)


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)


class Client(models.Model):
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    is_active = models.BooleanField(default=True)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_legajo = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)


class Coordinator(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni_number = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)