from student import Student
from academic_performance import AcademicPerformance
from desired_performance import DesiredPerformance
import json
import xml.etree.ElementTree as ET


class StudentFullInfo(Student, AcademicPerformance, DesiredPerformance):

    def __init__(self, name, date_of_birth, group, list_of_subjects,
                 list_of_grades, list_of_desired_grades):
        Student.__init__(self, name, date_of_birth, group)
        AcademicPerformance.__init__(self, list_of_subjects, list_of_grades)
        DesiredPerformance.__init__(self, list_of_subjects,
                                    list_of_desired_grades)
        self.list_of_desired_grades = list_of_desired_grades

    def __str__(self):
        return (
            f"Student: {self.name}, Date of birth: {self.date_of_birth}, "
            f"Group: {self.group}, List of subjects: {self.list_of_subjects}, "
            f"List of grades: {self.list_of_grades}, Desired grades: {self.list_of_desired_grades}, "
            f"Average mark: {self.average_mark():.3f}, Average desired mark: {self.average_desired_mark():.3f}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "group": self.group,
            "list_of_subjects": self.list_of_subjects,
            "list_of_grades": self.list_of_grades,
            "list_of_desired_grades": self.list_of_desired_grades,
            "average_mark": f"{self.average_mark():.3f}",
            "average_desired_mark": f"{self.average_desired_mark():.3f}"
        }

    def save(self, file_path, file_format='json'):
        data = self.to_dict()
        if file_format == 'json':
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
        elif file_format == 'xml':
            root = ET.Element("Student")
            for key, value in data.items():
                child = ET.SubElement(root, key)
                child.text = str(value)
            tree = ET.ElementTree(root)
            tree.write(file_path)
        else:
            raise ValueError("Unsupported file format. Use 'json' or 'xml'.")
