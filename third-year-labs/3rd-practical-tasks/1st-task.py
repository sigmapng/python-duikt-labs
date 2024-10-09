class Student:

    def __init__(
        self,
        name,
        date_of_birth,
        group,
    ):
        self.name = name
        self.date_of_birth = date_of_birth
        self.group = group


class Academic_performance:

    def __init__(self, list_of_subjects, list_of_grades):
        self.list_of_subjects = list_of_subjects
        self.list_of_grades = list_of_grades

    def average_mark(self):
        return sum(self.list_of_grades) / len(self.list_of_grades)
