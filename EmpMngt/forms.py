from django import forms
from .models import Employee,EmployeeSalary

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  


class SalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = ['salary', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
