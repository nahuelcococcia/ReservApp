from django.contrib import admin
from .models import Service

# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'is_active')
    search_fields = ['name']
    list_filter = ['is_active']
