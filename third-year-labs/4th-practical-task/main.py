from csv_reader import CsvReader
from data_analyzer import DataAnalyzer
from data_preprocessor import DataPreprocessor
from data_uploader import DataUploader
from database_initializer import DatabaseInitializer
from database_queries import DatabaseQueries
from tabulate import tabulate

db_initializer = DatabaseInitializer()
db_initializer.create_tables()
db_initializer.close()

csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
csv_reader = CsvReader()
data = csv_reader.read_data(csv_url)
preprocessor = DataPreprocessor(data)
processed_data = preprocessor.add_student_ids()

analyzer = DataAnalyzer(processed_data)
students = analyzer.get_students()
courses = analyzer.get_courses()
grades = analyzer.get_grades()

uploader = DataUploader()
uploader.upload_students(students)
uploader.upload_courses(courses)
uploader.upload_grades(grades)
uploader.close()

queries = DatabaseQueries()

student = queries.find_student_by_last_name("Єфимов")
if student:
    print(f"Знайдений студент: {student[0][1]} {student[0][2]}")

    student_id = student[0][0]
    student_grades = queries.get_student_grades(student_id)

    headers = ["Курс", "Оцінка"]
    print(tabulate(student_grades, headers=headers, tablefmt="plain"))

queries.close()
