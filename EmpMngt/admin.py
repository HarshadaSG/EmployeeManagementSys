from django.contrib import admin
from .models import Department, Employee, EmployeeSalary

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor')

admin.site.register(Department, DepartmentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'designation', 'department', 'reporting_manager')

admin.site.register(Employee, EmployeeAdmin)

class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'start_date', 'end_date')

admin.site.register(EmployeeSalary, EmployeeSalaryAdmin)
