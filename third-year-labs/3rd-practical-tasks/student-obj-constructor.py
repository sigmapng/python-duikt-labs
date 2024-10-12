from abc import ABC, abstractmethod

class Student:
    def __init__(self, name, date_of_birth, group):
        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__group = group

    @property
    def name(self):
        return self.__name

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def group(self):
        return self.__group


class AcademicPerformance(ABC):
    @abstractmethod
    def __init__(self, list_of_subjects, list_of_grades):
        self.list_of_subjects = list_of_subjects
        self.list_of_grades = list_of_grades

    def average_mark(self):
        return sum(self.list_of_grades) / len(self.list_of_grades)


class DesiredPerformance(AcademicPerformance):
    def __init__(self, list_of_subjects, list_of_grades):
        super().__init__(list_of_subjects, list_of_grades)

    def input_desired_grades(self):
        self.input_subject = input("Enter the desired grade for each subject: ")


class StudentFullInfo(Student, AcademicPerformance):
    def __init__(self, name, date_of_birth, group, list_of_subjects, list_of_grades):
        Student.__init__(self, name, date_of_birth, group)
        AcademicPerformance.__init__(self, list_of_subjects, list_of_grades)

    def __str__(self):
        return (f"Student: {self.name}, Date of birth: {self.date_of_birth}, "
                f"Group: {self.group}, Average mark: {self.average_mark()}")
