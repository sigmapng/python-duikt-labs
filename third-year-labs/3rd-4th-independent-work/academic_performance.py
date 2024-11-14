from performance import Performance


class AcademicPerformance(Performance):

    def __init__(self, list_of_subjects, list_of_grades):
        super().__init__(list_of_subjects, list_of_grades)

    def average_mark(self):
        return sum(self.list_of_grades) / len(self.list_of_grades)
