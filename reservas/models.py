from django.db import models
from datetime import datetime


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)


class Client(models.Model):
    name = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    is_active = models.BooleanField(default=True)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    file_number = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def fullname(self):
        return f'{self.name} {self.lastname}'


class Coordinator(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dni_number = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)

    def fullname(self):
        return f'{self.name} {self.lastname}'


class ReserveService(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    reservation_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # responsible = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
