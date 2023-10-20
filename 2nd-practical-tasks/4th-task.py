# Dictionaries

#4.1
studentData = {}

while True:
    studentName = input("\nEnter the student's name (or press Enter to finish): ")
    
    # We check if the user pressed Enter to finish
    if not studentName:
        break
    
    studentGrade = float(input("Enter the student's grade: "))
    
    # We save data about the student in the dictionary
    studentData[studentName] = studentGrade

print("\nData about students:")
for name, grade in studentData.items():
    print(f"Name: {name}, grade: {grade}")

#4.2
studentDataImproved = {}

while True:
    studentName = input("\nEnter the student's name (or press Enter to finish): ")

    # We check if the user pressed Enter to finish
    if not studentName:
        break
    
    studentGrades = []
    while True:
        gradeInput = input("Enter the student's grade (or press Enter to finish): ")
        if not gradeInput:
            break
        try:
            grade = float(gradeInput)
            studentGrades.append(grade)
        except ValueError:
            print("\nIncorrect grade format. Please enter a numeric value.")

    studentDataImproved[studentName] = studentGrades

print("\nData about students:")
for name, grades in studentDataImproved.items():
    averageGrade = sum(grades) / len(grades)
    print(f"Name: {name}, Grades: {grades}, Arithmetic mean: {averageGrade}")
