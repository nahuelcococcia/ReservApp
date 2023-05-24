from django.contrib import admin
from django.urls import path
from reservas import views

urlpatterns = [
    path('home/', views.index, name="home"),
    path('employee/new/', views.employee_register), 
    path('employee/activate/<int:id>/', views.employee_activate, name="employee-activate"), 
    path('employee/update/<int:employee_id>', views.employee_update, name="employee-update"),
    path('employee/deactivate/<int:employee_id>', views.employee_deactivate, name="employee-deactivate"),
    path('employees/list/', views.employees_view),
    path('coordinator/deactivate/<int:coordinator_id>/', views.coordinator_deactivate, name='coordinator-deactivate'),
    path('coordinator/activate/<int:coordinator_id>/', views.coordinator_activate, name='coordinator-activate'),

]          
