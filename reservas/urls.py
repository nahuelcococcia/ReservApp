from django.contrib import admin
from django.urls import path
from reservas import views

urlpatterns = [
    path('home/', views.index, name="home"),
    path('employee/new/', views.employee_register, name="employee-create"),
    path('employee/activate/<int:id>/', views.employee_activate, name="employee-activate"), 
    path('employee/update/<int:employee_id>/', views.employee_update, name="employee-update"),
    path('employee/delete/<int:employee_id>/', views.employee_delete, name="employee-delete"),
    path('employee/deactivate/<int:employee_id>', views.employee_deactivate, name="employee-deactivate"),
    path('employees/list/', views.employees_view, name="employee-list"),
    path('coordinator/new/', views.coordinator_register, name="coordinator-create"),
    path('coordinators/list/', views.coordinators_view, name="coordinators-list"),
    path('coordinator/update/<int:coordinator_id>/', views.coordinator_update, name="coordinator-update"),
    path('coordinator/deactivate/<int:coordinator_id>/', views.coordinator_deactivate, name='coordinator-deactivate'),
    path('coordinator/activate/<int:coordinator_id>/', views.coordinator_activate, name='coordinator-activate'),
    path('coordinator/delete/<int:coordinator_id>/', views.coordinator_delete, name="coordinator-delete"),
    path('client/activate/<int:client_id>/', views.client_activate, name="client-activate"),
    path('client/deactivate/<int:client_id>/', views.client_deactivate, name="client-deactivate"),
]

