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
    path('clients/list/', views.clients_view, name="clients-list"),
    path('client/new/', views.client_register, name="client-create"),
    path('client/update/<int:client_id>/', views.client_update, name="client-update"),
    path('client/activate/<int:client_id>/', views.client_activate, name="client-activate"),
    path('client/deactivate/<int:client_id>/', views.client_deactivate, name="client-deactivate"),
    path('client/delete/<int:client_id>/', views.client_delete, name="client-delete"),
    path('services/list/', views.service_view, name='services-list'),
    path('service/new/', views.service_register, name="service-create"),
    path('service/update/<int:service_id>/', views.service_update, name="service-update"),
    path('service/activate/<int:service_id>/', views.service_activate, name="service-activate"),
    path('service/deactivate/<int:service_id>/', views.service_deactivate, name="service-deactivate"),
    path('service/delete/<int:service_id>/', views.service_delete, name="service-delete"),
    path('reserves/list/', views.reserves_view, name="reserves-list"),
    path('reserve/new/', views.reserve_register, name="reserve-create"),
    path('reserve/update/<int:reserve_id>', views.reserve_update, name="reserve-update"),
    path('reserve/delete/<int:reserve_id>/', views.reserve_delete, name="reserve-delete"),

]

