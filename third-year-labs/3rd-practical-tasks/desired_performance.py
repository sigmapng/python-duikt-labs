from performance import Performance


class DesiredPerformance(Performance):

    def __init__(self, list_of_subjects, list_of_desired_grades):
        super().__init__(list_of_subjects, list_of_desired_grades)

    def average_desired_mark(self):
        return sum(self.list_of_grades) / len(self.list_of_grades)
