# 4. Dictionaries:
""" 4.1 Write a program where the user enters the name of the student and his grade.
The program stores this data in a dictionary, where the key is the student's name. User
can continue to enter students or end entry. After completion
input, the program should output the names of the students and their grades. """
students = {}

while True:
    name = input("Enter the student's name (or type 'end' to finish): ")
    if name.lower() == 'end':
        break
    grade = input(f"Enter the grade for {name}: ")
    students[name] = grade

print("\nStudent Grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")
""" 4.2 Write a program that creates a dictionary from the number of occurrences
of each character in the string entered by the user. """
string = input("Enter a string: ")
char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("\nCharacter Count:")
for char, count in char_count.items():
    print(f"{char}: {count}")
