from django.db import models


# Create your models here.
class Modelo1(models.Model):
    campo1 = models.CharField(max_length=50)


class Client(models.Model):
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    is_active = models.BooleanField(default=True)
