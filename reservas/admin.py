from django.contrib import admin
from .models import Service, Client


# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'is_active')
    search_fields = ['name']
    list_filter = ['is_active']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'is_active')
    search_fields = ('name', 'last_name')
    list_filter = ['is_active']

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'numero_legajo', "activo")
    search_fields = ('nombre', 'apellido')
    list_filter = ['activo']
