import math

x = int(input("Please enter x to define z: "))
t = 1

# Equation z = (9πt + 10cos(x) / √t - |sin(t)|) e^x
zEquation = float((9 * math.pi * t + (10 * math.cos(x)))/(math.sqrt(t)-abs(math.sin(t)))*math.exp(x))
zEquationResultRounded = round(zEquation, 2)

print("Therefore, Z equals:", zEquationResultRounded)