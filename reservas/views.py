from django.shortcuts import render, redirect

# Create your views here.
# Considero que el Form de empleado se llama EmployeeForm


def employee_update_view(request, employee_id):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
    employee = Employee.objects.get(id=employee_id)
    form = EmployeeForm(instance=employee)
    return render(request, 'employee_update.html', {
        'form': form,
        'submit': 'Actualizar'
    })

