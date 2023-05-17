from django.contrib import admin
from .models import Coordinator


@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'dni_number', 'is_active')
    search_fields = ['name', 'lastname']
    list_filter = ['is_active']

