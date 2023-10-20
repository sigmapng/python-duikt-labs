# Functions

#5.1, 5.2
def getStudentName():
    studentName = input("\nEnter the student's name (or press Enter to finish): ")
    return studentName

def getStudentGrades():
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
    return studentGrades

def calculateAverage(grades):
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0.0

def main():
    studentDataImproved = {}
    
    while True:
        studentName = getStudentName()
    
        if not studentName:
            break
    
        studentGrades = getStudentGrades()
        studentDataImproved[studentName] = studentGrades
    
    print("\nData about students:")
    for name, grades in studentDataImproved.items():
        averageGrade = calculateAverage(grades)
        print(f"Name: {name}, Grades: {grades}, Arithmetic mean: {averageGrade}")

if __name__ == "__main__":
    main()

