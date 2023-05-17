from django.db import models


# Create your models here.
class Modelo1(models.Model):
    campo1 = models.CharField(max_length=50)


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
