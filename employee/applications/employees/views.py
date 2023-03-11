from django.shortcuts import render
from django.views.generic import ListView

from .models import Employee

class EmployeesListView(ListView):
    template_name = 'employees/list_employees.html'
    model = Employee

# Create your views here.
