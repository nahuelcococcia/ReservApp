from django.urls import path
from api import views

urlpatterns = [
    path('services/', views.api_service),
    path('services/<int:service_id>/', views.api_service_id),
    path('clients/', views.api_client),
    path('employees/', views.api_employee),
    path('coordinators/', views.api_coordinator),
]

