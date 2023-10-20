# Working with lists

import math

#3.1
inputStr = input("Enter a sequence of numbers separated by commas: ")

numbersStr = inputStr.split(',')
numbers = [float(num.strip()) for num in numbersStr]

numList = numbers
numTuple = tuple(numbers)
print("List of numbers: ", numList)
print("Tuple of numbers:", numTuple)

total = sum(numbers)
average = total / len(numbers)
print("Sum of numbers:", total)
print("Arithmetic mean:", average)

#3.2
n = int(input("Enter your n value: "))
squares = [i ** 2 for i in range(1, n + 1)]

print("List of squares of numbers from 1 to", n, ":", squares)
