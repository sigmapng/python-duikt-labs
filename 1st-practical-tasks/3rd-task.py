import math

def calculate_function (x):
    if x >= 0:
        func_result = 0.5 - math.pow(abs(x), 0.25)
    elif x < 0:
        func_result = (math.pow(math.sin(x), 2) * pow(x, 2)) / abs(x + 1)

    round_func_result = round(func_result, 2)
    return round_func_result

x = int(input ("Please, enter a value for x: "))
result = calculate_function(x)
print("Therefore, answer is:", result)
