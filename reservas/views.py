from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return HttpResponse("<h1> Hola Mundo </h1>")

def employee_register(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            return redirect('home')  # Redirect to a success page after registration
    form = EmployeeForm()
    return render(request, 'employee_register.html', {
        'form': form,
         "submit": "Registrar Empleado"
         })