from django.contrib import admin
from .models import Service, Client, ReserveService


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


@admin.register(ReserveService)
class ReserveServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'creation_date', 'reservation_date', 'client', 'employee', 'service', 'price')
    search_fields = ['client', 'employee', 'service']

