from django.contrib import admin
from django.urls import path
from reservas import views

urlpatterns = [
    path('home/', views.index, name="home"),
    path('employee/new/', views.employee_register), 
    path('employee/activate/<int:id>/', views.employee_activate, name="employee-activate"), 
    
    
]
