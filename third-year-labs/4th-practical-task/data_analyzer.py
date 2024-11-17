class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_students(self):
        students = [
            {
                'ID': student['ID'],
                'first_name': student["Ім'я"],
                'last_name': student['Прізвище'],
            }
            for student in self.data
        ]
        return students

    def get_courses(self):
        courses_set = set()
        for student in self.data:
            for key in student.keys():
                if key.startswith("Завдання"):
                    course_name = key.split(" ")[2:-2]
                    course_name = " ".join(course_name)
                    courses_set.add(course_name)

        courses_list = [{"name": name, "number": int(
            name.split(" ")[0][1:])} for name in courses_set]

        sorted_courses = sorted(courses_list, key=lambda x: x["number"])

        courses = [{'id': idx + 1, 'name': course['name']}
                   for idx, course in enumerate(sorted_courses)]

        return courses

    def get_grades(self):
        grades = {}
        for student in self.data:
            student_grades = {}
            for key, value in student.items():
                if key.startswith("Завдання"):
                    task_id = int(key.split("№")[1].split(" ")[0])
                    student_grades[task_id] = value
            grades[student['ID']] = student_grades
        return grades
