# 5. Functions:
""" 5.1 Write a function that takes a list of numbers as an argument and returns
the maximum number, the minimum number, and the arithmetic mean of these numbers. """


def analyze_numbers(numbers):
    if not numbers:
        return None, None, None
    max_num = max(numbers)
    min_num = min(numbers)
    mean_num = sum(numbers) / len(numbers)
    return max_num, min_num, mean_num


""" 5.2 *Write a function that takes a list of numbers and a number n as arguments.
The function should return True if the sum of any two numbers from the list
is equal to the given number n, or False otherwise. """


def check_pair_with_sum(numbers, n):
    seen = set()
    for number in numbers:
        if n - number in seen:
            return True
        seen.add(number)
    return False
