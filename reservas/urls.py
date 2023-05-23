from django.contrib import admin
from django.urls import path
from .views import index, employees_view, employee_register

urlpatterns = [
    path('home/', views.index, name="home"),
    path('employee/new/', views.employee_register), 
    path('employee/activate/<int:id>/', views.employee_activate, name="employee-activate"), 
    path('employee/update/<int:employee_id>', views.employee_update, name="employee-update"),
    path('employees/list/', employees_view) 
]
