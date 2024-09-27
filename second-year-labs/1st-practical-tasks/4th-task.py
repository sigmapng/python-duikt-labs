"""
Created a function get_user_input to handle user input and ensure that the input is a valid integer.
"""
def getUserInput(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid integer.")

"""
Created a function check_and_print to handle the common logic of checking whether a number is in the list and printing the result.
Used f-strings for string formatting.
"""
def checkAndPrint(number, number_range, ordinal):
    if number in number_range:
        print(f"\nYes, your {ordinal} number is in this range: {number_range}")
    else:
        print(f"\nNo, your {ordinal} number is not in this range: {number_range}")

def main():
    indicator_of_range_limit = getUserInput("Please enter the number that will be the limit of your number range: ")
    num_range = list(range(1, indicator_of_range_limit + 1))

    num_1 = getUserInput("Now, enter num 1: ")
    num_2 = getUserInput("Now, enter num 2: ")
    num_3 = getUserInput("Now, enter num 3: ")

    checkAndPrint(num_1, num_range, "first")
    checkAndPrint(num_2, num_range, "second")
    checkAndPrint(num_3, num_range, "third")

""" 
if __name__ == "__main__": block is a common Python idiom used to determine whether the Python script is being run as the main program 
or if it is being imported as a module into another script. 
"""
if __name__ == "__main__":
  main()
