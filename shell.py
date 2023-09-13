from django.db.models import Avg, Max, Min, Sum, Count, F, ExpressionWrapper, DecimalField, CharField, Case, When, Value
from datetime import date, timedelta
from check_employee.models import *

from check_employee.models import *

employees_sorted_salary = Employee.objects.order_by('-salary')

it_department = Department.objects.get(name='IT_department')
web_designer = Positions.objects.get(name='Web Designer')
navuhodonosor = Employee(
    fullname='Навуходоно́сор',
    birth_date="1990-01-01",
    receipt_date="2020-01-01",
    salary=50000,
    department=it_department,
    position=web_designer
)
navuhodonosor.save()

employees_sorted_by_birth_receipt_date = Employee.objects.order_by('-birth_date', 'receipt_date')

employee_in_salary_range=Employee.objects.filter(salary__gte=20000, salary__lte=50000)

accounting_employee = Employee.objects.filter(department_id=3).order_by('fullname')

accounting_department = Department.objects.get(name='accounting_department')


departments = Department.objects.annotate(employee_count=Count('employee')).order_by('employee_count')

departments_employee_count = Employee.objects.values('department__name').annotate(
    department_count=Count('id')).order_by('department_count')


department_avg_salary = Employee.objects.values('department__name').annotate(
    average_salary=Avg('salary')).order_by('average_salary')

employees = Employee.objects.values('fullname','salary', 'receipt_date','departments').annotate(

)

#
# accounting_employee = Employee.objects.filter(department__name='accounting_department').order_by(
#     Case(
#         When(fullname='', then=Value(' ')),
#         default=F('fullname'),
#         output_field=CharField()
