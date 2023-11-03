from employees_and_managers import employees_list, Manager

for employee in employees_list:
    if isinstance(employee, Manager):
        report = employee.generate_report()
        print(report)
