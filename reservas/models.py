from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def fullname(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return self.fullname()


class Employee(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    file_number = models.IntegerField(unique=True, error_messages={
        'unique': "Ya existe Empleado con ese Numero de legajo."
    })
    is_active = models.BooleanField(default=True)

    def fullname(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return self.fullname()


class Coordinator(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dni_number = models.IntegerField(unique=True, error_messages={
        'unique': "Ya existe Coordinador con ese DNI."
    })
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def fullname(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return self.fullname()


class ReserveService(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    reservation_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    responsible = models.ForeignKey(Coordinator, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'Cliente: {self.client}, Servicio: {self.service}, Precio: {self.price}'
