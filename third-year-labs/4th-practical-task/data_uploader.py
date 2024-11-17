import sqlite3
import os


class DataUploader:
    def __init__(self, db_name="university.db"):
        self.db_name = os.path.join(os.path.dirname(__file__), db_name)
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def upload_students(self, students):
        self.cursor.executemany('INSERT OR REPLACE INTO students (ID, first_name, last_name) VALUES (?, ?, ?)',
                                [(student['ID'], student['first_name'], student['last_name']) for student in students])
        self.conn.commit()

    def upload_courses(self, courses):
        self.cursor.executemany('INSERT OR REPLACE INTO courses (id, name) VALUES (?, ?)',
                                [(course['id'], course['name']) for course in courses])
        self.conn.commit()

    def upload_grades(self, grades):
        for student_id, student_grades in grades.items():
            for course_id, grade in student_grades.items():
                self.cursor.execute('INSERT OR REPLACE INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)',
                                    (student_id, course_id, grade))
        self.conn.commit()

    def close(self):
        self.conn.close()
