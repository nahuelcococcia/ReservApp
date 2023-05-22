from django.contrib import admin
from django.urls import path
from .views import index, employees_view, employee_register

urlpatterns = [
    path('home/', index, name="home"),
    path('employee/new/', employee_register),
    path('employees/list/', employees_view)
    
]
