from django.db import models
from datetime import datetime


class Coordinator(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dni_number = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)
