# 1.Simple Validation and loops
""" 1.1 Write a program that asks the user for his age. If age is less than 18,
the program should display "You are still a minor", otherwise - "You are an adult" """
print("Hi, we want to check if you are an adult!")
user_age = int(input("Please enter your age: "))


def check_user_age(n):
    if n >= 18:
        print("You are an adult")
    else:
        print("You are still a minor")
    return


check_user_age(user_age)
""" 1.2 Write a program that displays a "pyramid" of stars on the screen. User
enters the height of the pyramid pyramid_height """
print("Hi, this program will make a pyramid for you!")
user_rows_num_input = int(
    input("Please enter a number of rows you would like to see: "))


def print_star_pyramid(n):
    star_symbol = "*"
    iteration_counter = 1

    while iteration_counter <= 2 * n - 1:
        spaces = ' ' * (n - (iteration_counter // 2) - 1)
        print(spaces + star_symbol * iteration_counter)
        iteration_counter += 2
    return


print_star_pyramid(user_rows_num_input)
