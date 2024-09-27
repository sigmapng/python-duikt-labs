import math

""" 
Function: f(x) = { 0.5 - 4^√|x|, x >= 0 //
                   sin^2x^2 / |x + 1|, x < 0
"""
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
