from student_obj_constructor import StudentFullInfo  #error: ModuleNotFoundError: No module named 'student_obj_constructor'


def create_student_profile():
    input_name = input("Enter your name: ")
    input_date_of_birth = input("Enter your date of birth: ")
    input_group = input("Enter your group: ")

    input_list_of_subjects = input(
        "Enter the list of subjects (comma-separated): ").split(',')
    input_list_of_subjects = [
        subject.strip() for subject in input_list_of_subjects
    ]

    while True:
        try:
            input_list_of_grades = list(
                map(
                    float,
                    input("Enter the list of grades (comma-separated): ").
                    split(',')))
            if len(input_list_of_grades) != len(input_list_of_subjects):
                raise ValueError(
                    "The number of grades must match the number of subjects.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    student_profile = StudentFullInfo(input_name, input_date_of_birth,
                                      input_group, input_list_of_subjects,
                                      input_list_of_grades)
    return student_profile


def print_student_profile(student_profile):
    print(student_profile)


if __name__ == "__main__":
    student_profile = create_student_profile()
    print_student_profile(student_profile)
