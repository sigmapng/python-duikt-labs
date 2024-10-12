from academic_performance import AcademicPerformance


class DesiredPerformance(AcademicPerformance):

    def __init__(self, list_of_subjects, list_of_grades):
        super().__init__(list_of_subjects, list_of_grades)

    def input_desired_grades(self):
        self.input_subject = input(
            "Enter the desired grade for each subject: ")
