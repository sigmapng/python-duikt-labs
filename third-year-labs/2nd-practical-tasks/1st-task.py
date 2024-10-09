# 1. Creation of the "Employee" class
""" 1.1. Create an Employee class with the following attributes: name, salary_salary,
number_of_worked_days.

1.2. Use the __init__ method to initialize attributes. """


class Employee:

    def __init__(self, name, salary, number_of_worked_days, bonus_percent=0):
        self.name = name
        self.salary = salary
        self.number_of_worked_days = number_of_worked_days
        self.bonus_percent = bonus_percent

    def calculate_monthly_salary(self):
        return (self.salary / 30) * self.number_of_worked_days

    def calculate_bonus(self):
        monthly_salary = self.calculate_monthly_salary()
        return (monthly_salary / 100) * self.bonus_percent


# 2. Class methods
""" 2.1. Add a method to the class that calculates the employee's monthly salary.
Monthly salary=(salary / 30) * number_of_worked_days

2.2 In the __init__ method, add an additional "bonus_percent" attribute for
saving a percentage of the bonus for the employee. Default is bonus_percent
must be equal to 0.

2.3. Add a method that calculates the employee's bonus based on the method
calculation of salary (from 2.1) according to the formula: Bonus = (Salary / 100) *
percentage _bonus """

# 3. Inheritance
""" 3.1. Create a Manager class that derives from the Employee class.

3.2. Add an additional attribute for the manager: "number of subordinates",
"reward_size" (reward_size - must be set in the class for all one without
the possibility of installing it in the object).

3.3. Add a report method that generates a report for the manager based on the quantity
his subordinates. The method should return a string in the format: "Manager [Name
manager] manages [a number of subordinate] employees." """


class Manager(Employee):
    reward_size = 1000

    def __init__(self,
                 name,
                 salary_salary,
                 number_of_worked_days,
                 number_of_subordinates,
                 bonus_percent=0):
        super().__init__(name, salary_salary, number_of_worked_days,
                         bonus_percent)
        self.number_of_subordinates = number_of_subordinates

    def generate_report(self):
        return f"Manager {self.name} manages {self.number_of_subordinates} employees."


# 4. Encapsulation
""" 4.1. Make attributes name, salary_salary, number_of_worked_days,
bonus_percentage (additionally for the Manager class - number of_subordinates) - protected.

4.2. Add getter and setter methods to access these attributes. """

# 5. Polymorphism
""" 5.1. Redefine the bonus calculation method in the Manager class so that it
took into account not only salary and days worked, but also the number of subordinates.
Bonus calculation formula: we accept the result from the bonus calculation method
(which was created in 2.3) and add ( + number_of_subordinates * amount_of_award ) """

# 6. Abstraction
""" 6.1. Create an abstract class "Person" with an abstract method for
salary calculation.

6.2. Make the Employee class a descendant of this abstract class and implement
it contains an abstract method for calculating salary. """

# 7. Working with objects
""" 7.1. Create several objects of class "Employee" and "Manager".

7.2. Add them to your employee list.

7.3. Demonstrate the calculation of salary and bonuses for each employee
from this list. """
