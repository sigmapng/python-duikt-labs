def employeesDaysWorked():
    works = {}
    while True:
        employeeName = input("Enter name of worker (or type 'stop' to stop): ")
        if employeeName.lower() == 'stop':
            break
        employeeSalary = float(input("Enter the employee's salary: "))
        daysWorked = int(input("Enter the number of days worked by the employee: "))
        works[employeeName] = {'employeeSalary': employeeSalary, 'daysWorked': daysWorked}
    return works
