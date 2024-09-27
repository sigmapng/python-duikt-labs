from main import Employee, Manager

employee1 = Employee("Alice", 3000, 25, 5, "Higher")
employee2 = Employee("Bob", 3500, 28, 8, "Secondary")
manager1 = Manager("Charlie", 4000, 26, 10, 5, "Administrator")
manager2 = Manager("David", 4500, 30, 12, 8, "Manager")
employee3 = Employee("Eve", 3200, 27, 6, "Higher")
employee4 = Employee("Frank", 3400, 29, 7, "Secondary")
manager3 = Manager("Grace", 4100, 27, 11, 6, "Administrator")
manager4 = Manager("Hank", 4600, 31, 14, 9, "Manager")
employee5 = Employee("Ivy", 3100, 24, 4, "Higher")
employee6 = Employee("Jack", 3300, 30, 9, "Secondary")

employees_list = [employee1, employee2, manager1, manager2, employee3, employee4, manager3, manager4, employee5, employee6]

for employee in employees_list:
    payment = employee.calculate_payment()
    bonus = employee.calculate_bonus()
    print(f"{employee.name}: Payment - {payment}, Bonus - {bonus}")
