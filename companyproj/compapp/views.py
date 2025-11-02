from django.shortcuts import render
from .models import Employee
# Create your views here.
def employee_view(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html',
                  {'employees': employees})