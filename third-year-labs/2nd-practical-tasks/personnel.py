from abc import ABC, abstractmethod

class Personnel(ABC):

    def __init__(self, name, salary, num_of_days_worked):
        self.name = name
        self.salary = salary
        self.num_of_days_worked = num_of_days_worked
        
        