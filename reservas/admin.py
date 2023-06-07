from django.contrib import admin
from .models import Service, Client, ReserveService, Employee, Coordinator


# La sentencia @admin.register(Model) es un decorador que registra un modelo en el panel del administrador
# por lo tanto cada que aparezca dicha sentencia se estara registrando un modelo, la finalidad es visualizarlo
# en la pantalla admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # Definimos la lista de atributos del modelo Service que mostraremos en el panel
    list_display = ('id', 'name', 'description', 'price', 'is_active')
    # Definimos al atributo name como criterio de búsqueda
    search_fields = ['name']
    # Definimos al atributo is_active como criterio de filtrado
    list_filter = ['is_active']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # Definimos la lista de atributos del modelo Client que mostraremos en el panel
    list_display = ('id', 'name', 'lastname', 'is_active')
    # Definimos a los atributos name y lastname, como criterio de búsqueda
    search_fields = ('name', 'lastname')
    # Definimos al atributo is_active como criterio de filtrado
    list_filter = ['is_active']


@admin.register(Employee)
class EmpleadoAdmin(admin.ModelAdmin):
    # Definimos la lista de atributos del modelo Employee que mostraremos en el panel
    list_display = ('id', 'name', 'lastname', 'file_number', "is_active")
    # Definimos  a los atributos name y lastname, como criterio de búsqueda
    search_fields = ('name', 'lastname')
    # Definimos al atributo is_active como criterio de filtrado
    list_filter = ['is_active']


@admin.register(ReserveService)
class ReserveServiceAdmin(admin.ModelAdmin):
    # Definimos la lista de atributos del modelo ReserveService que mostraremos en el panel
    list_display = ('id', 'creation_date', 'reservation_date', 'client', 'responsible', 'employee', 'service', 'price')
    # Definimos a los atributos client, employee, service y responsible como criterio de búsqueda
    search_fields = ['client', 'employee', 'service', 'responsible']


@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    # Definimos la lista de atributos del modelo Coordinator que mostraremos en el panel
    list_display = ('id', 'name', 'lastname', 'dni_number', "created_at", "is_active")
    # Definimos  a los atributos name y lastname, como criterio de búsqueda
    search_fields = ('name', 'lastname')
    # Definimos al atributo is_active como criterio de filtrado
    list_filter = ['is_active']

# Se puede también en list_display reemplazar en algunos casos por la siguiente sentencia
# list_display = [field.name for field in MiModelo._meta.fields]
# Esto llenaria la lista para mostrar con todos los atributos del modelo llamado MiModelo
