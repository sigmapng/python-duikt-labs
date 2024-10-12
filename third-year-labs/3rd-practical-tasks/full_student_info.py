from student import Student
from academic_performance import AcademicPerformance


class StudentFullInfo(Student, AcademicPerformance):

    def __init__(self, name, date_of_birth, group, list_of_subjects,
                 list_of_grades):
        Student.__init__(self, name, date_of_birth, group)
        AcademicPerformance.__init__(self, list_of_subjects, list_of_grades)

    def __str__(self):
        return (f"Student: {self.name}, Date of birth: {self.date_of_birth}, "
                f"Group: {self.group}, Average mark: {self.average_mark()}")
