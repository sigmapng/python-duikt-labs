import os
from student_full_info import StudentFullInfo


def create_student_profile():
    input_name = input("Enter your name: ")
    input_date_of_birth = input("Enter your date of birth: ")
    input_group = input("Enter your group: ")

    input_list_of_subjects = input("Enter the list of subjects (comma-separated): ").split(',')
    input_list_of_subjects = [subject.strip() for subject in input_list_of_subjects]

    while True:
        try:
            input_list_of_grades = list(map(float, input("Enter the list of grades (comma-separated): ").split(',')))
            if len(input_list_of_grades) != len(input_list_of_subjects):
                raise ValueError("The number of grades must match the number of subjects.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    while True:
        try:
            input_list_of_desired_grades = list(map(float, input("Enter the list of desired grades (comma-separated): ").split(',')))
            if len(input_list_of_desired_grades) != len(input_list_of_subjects):
                raise ValueError("The number of desired grades must match the number of subjects.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    student_profile = StudentFullInfo(input_name, input_date_of_birth, input_group, input_list_of_subjects, input_list_of_grades, input_list_of_desired_grades)
    return student_profile


def print_student_profile(student_profile):
    print(student_profile)


def save_student_profile(student_profile):
    file_format = input("Enter the file format to save (json/xml): ").strip().lower()
    directory = "third-year-labs/3rd-practical-tasks/converted-files"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, f"{student_profile.name}.{file_format}")
    student_profile.save(file_path, file_format)
    print(f"Student profile saved to {file_path}")


if __name__ == "__main__":
    student_profile = create_student_profile()
    print_student_profile(student_profile)
    save_student_profile(student_profile)
