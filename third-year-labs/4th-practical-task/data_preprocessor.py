class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def add_student_ids(self):
        for index, student in enumerate(self.data, start=1):
            student['ID'] = index
        return self.data
