from django.urls import path
from . import views

employees_patterns = ([
    path('',views.EmployeesListView.as_view(),name = 'list'),
],"employees")
