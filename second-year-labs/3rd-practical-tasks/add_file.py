def calculateAverageSalary(works):
    employeeSalaryMatrix = []
    for name, details in works.items():
        nameData = [name, details['daysWorked'], (details['employeeSalary'] / 30) * details['daysWorked']]
        employeeSalaryMatrix.append(nameData)
    return employeeSalaryMatrix
