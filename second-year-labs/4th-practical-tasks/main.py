class Employee:
    def __init__(self, name, payment, worked_days, bonus_percentage=0, education_level="unknown"):
        self.name = name
        self.payment = payment
        self.worked_days = worked_days
        self.bonus_percentage = bonus_percentage
        self.education_level = education_level

    def calculate_payment(self):
        return (self.payment / 30) * self.worked_days

    def calculate_bonus(self):
        return (self.payment / 100) * self.bonus_percentage


class Manager(Employee):
    productivity_bonus_size = 500

    def __init__(self, name, payment, worked_days, bonus_percentage=0, subordinates=0, access_level="standard"):
        super().__init__(name, payment, worked_days, bonus_percentage)
        self.subordinates = subordinates
        self.access_level = access_level

    def generate_report(self):
        return f"Manager {self.name} supervises {self.subordinates} employees."
