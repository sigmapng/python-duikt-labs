import sqlite3
import os


class DatabaseInitializer:
    def __init__(self, db_name="university.db"):
        self.db_name = os.path.join(os.path.dirname(__file__), db_name)
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                ID INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                student_id INTEGER,
                course_id INTEGER,
                grade TEXT,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES students(ID),
                FOREIGN KEY (course_id) REFERENCES courses(id)
            )
        ''')

        self.conn.commit()

    def close(self):
        self.conn.close()
