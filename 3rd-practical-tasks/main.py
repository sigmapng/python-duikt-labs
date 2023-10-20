from secondary import employeesDaysWorked
from add_file import calculateAverageSalary

def printEmployeesData(employeeData):
    print("Matrix of employees:")
    for employee in employeeData:
        print(employee)
        
def main():
    daysWorked = employeesDaysWorked()
    salaryMatrix = calculateAverageSalary(daysWorked)
    printEmployeesData(salaryMatrix)
    
main()
