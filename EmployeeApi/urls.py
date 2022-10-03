from django.urls import path
from EmployeeApi import views

urlpatterns = [
    path('Employees/<int:id>',views.EmployeeById),
    path('Employees',views.Employees)
]