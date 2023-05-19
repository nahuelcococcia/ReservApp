from django.db import models


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


class ReserveService(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    reservation_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # responsible = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    employee = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
