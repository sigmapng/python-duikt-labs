# 3.Working with lists
""" 3.1 The user enters a sequence of numbers separated by commas. Program
should output a list of these numbers and then a tuple. Additionally, the program
should output the sum and arithmetic mean of these numbers. """
input_sequence = input("Enter a sequence of numbers separated by commas: ")

numbers_list = [float(num) for num in input_sequence.split(',')]

numbers_tuple = tuple(numbers_list)

total_sum = sum(numbers_list)
arithmetic_mean = total_sum / len(numbers_list)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)
print("Sum:", total_sum)
print("Arithmetic Mean:", arithmetic_mean)
""" 3.2 The user enters the number n. The program must generate
list of squares of numbers from 1 to n using a list generator. """

n = int(input("Enter a number n: "))

squares_list = [i**2 for i in range(1, n + 1)]

print("List of squares:", squares_list)
