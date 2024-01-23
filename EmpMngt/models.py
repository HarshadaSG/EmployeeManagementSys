from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation_choices = [('Associate', 'Associate'), ('Team Lead', 'Team Lead'), ('Manager', 'Manager')]
    designation = models.CharField(max_length=10, choices=designation_choices)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
