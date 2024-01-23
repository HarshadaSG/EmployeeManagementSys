"""
URL configuration for EMs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from EmpMngt import views
from django.urls import path

urlpatterns = [
    path('', views.admin_portal, name='admin_portal'),
    path('department_hierarchy/', views.department_hierarchy, name='department_hierarchy'),
    path('salary_costs_report/', views.salary_costs_report, name='salary_costs_report'),
    path('employee_details/',views.employee_details, name='employee_details'),
    path('update_salary/<int:salary_id>/',views.update_salary, name='update_salary'),
    path('delete_salary/<int:salary_id>/', views.delete_salary, name='delete_salary'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    
]
