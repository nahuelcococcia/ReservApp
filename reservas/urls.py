from django.contrib import admin
from django.urls import path
from reservas import views

urlpatterns = [
    path('home/', views.index, name="home"),
    path('employee/new/', views.employee_register),
    path('employee/deactivate/<int:employee_id>', views.employee_deactivate, name="employee-deactivate"),
]
