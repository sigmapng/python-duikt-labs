# 1.Simple Validation and loops

# 1.1
print("Hi, we want to check if you are an adult!")
user_age = int(input("Please enter your age: "))


def check_user_age(n):
    if n >= 18:
        print("You are old enough")
    else:
        print("Sorry, you are underage")
    return


check_user_age(user_age)

# 1.2
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

# 2.Strings

# 3.Working with lists

# 4.Dictionaries

# 5.Functions
