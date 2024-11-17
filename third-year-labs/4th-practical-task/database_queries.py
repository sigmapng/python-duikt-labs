import sqlite3
import os


class DatabaseQueries:
    def __init__(self, db_name="university.db"):
        self.db_name = os.path.join(os.path.dirname(__file__), db_name)
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def find_student_by_last_name(self, last_name):
        self.cursor.execute(
            'SELECT * FROM students WHERE last_name = ?', (last_name,))
        return self.cursor.fetchall()

    def get_student_grades(self, student_id):
        self.cursor.execute('''
            SELECT courses.name, grades.grade
            FROM grades
            JOIN courses ON grades.course_id = courses.id
            WHERE grades.student_id = ?
        ''', (student_id,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
