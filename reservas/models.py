from django.db import models


# Create your models here.
class Modelo1(models.Model):
    campo1 = models.CharField(max_length=50)