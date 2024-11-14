from abc import ABC, abstractmethod


class Performance(ABC):

    def __init__(self, list_of_subjects, list_of_grades):
        self.list_of_subjects = list_of_subjects
        self.list_of_grades = list_of_grades

    def average_mark(self):
        return sum(self.list_of_grades) / len(self.list_of_grades)

    @abstractmethod
    def save(self, file_path):
        pass
