from abc import ABC, abstractmethod
from student import Student

class AcademicPerformance(ABC):
    @abstractmethod
    def __init__(self, list_of_subjects, list_of_grades):
        self.list_of_subjects = list_of_subjects
        self.list_of_grades = list_of_grades

    def average_mark(self):
        return sum(self.list_of_grades) / len(self.list_of_grades)

