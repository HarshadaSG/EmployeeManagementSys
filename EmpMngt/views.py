from django.shortcuts import render
from .models import Department, Employee, EmployeeSalary
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SalaryForm
from django.db.models import Prefetch
from .models import Employee, EmployeeSalary
from .forms import EmployeeForm 


def admin_portal(request):
    return render(request, 'admin_portal.html')


def department_hierarchy(request):
    departments = Department.objects.all()

    hierarchy = {}
    for department in departments:
        manager = Employee.objects.filter(department=department, designation='Manager').first()
        team_leads = Employee.objects.filter(department=department, designation='TL')
        associates = Employee.objects.filter(department=department, designation='Associate')
        
        hierarchy[department.name] = {
            'manager': manager,
            'team_leads': team_leads,
            'associates': associates
        }

    return render(request, 'department_hierarchy.html', {'hierarchy': hierarchy})

def salary_costs_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        departments = Department.objects.all()

        cost_report = {}
        for department in departments:
            employees = Employee.objects.filter(department=department)
            total_cost = 0

            for employee in employees:
                salaries = EmployeeSalary.objects.filter(
                    employee=employee,
                    start_date__lte=end_date,
                    end_date__gte=start_date
                )

                for salary in salaries:
                    total_cost += salary.salary

            cost_report[department.name] = total_cost

        return render(request, 'salary_costs_report.html', {'cost_report': cost_report})

    return render(request, 'salary_costs_report.html')


def employee_details(request):
    employees = Employee.objects.prefetch_related(
        Prefetch('employeesalary_set', queryset=EmployeeSalary.objects.all(), to_attr='employee_salaries')
    ).all()

    return render(request, 'employee_details.html', {'employees': employees})


def update_salary(request, salary_id):
    salary = get_object_or_404(EmployeeSalary, id=salary_id)
    return redirect('employee_details')
def delete_salary(request, salary_id):
    salary = get_object_or_404(EmployeeSalary, id=salary_id)
    salary.delete()

    return redirect('employee_details')


def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_details')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'update_employee.html', {'form': form, 'employee': employee})





def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_details')

    return render(request, 'delete_employee.html', {'employee': employee})





def update_salary(request, salary_id):
    salary = get_object_or_404(EmployeeSalary, pk=salary_id)

    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('employee_details') 
    else:
        form = SalaryForm(instance=salary)

    return render(request, 'update_salary.html', {'form': form})