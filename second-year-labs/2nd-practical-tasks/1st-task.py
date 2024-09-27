# Simple check and loops

#1.1
age = int(input("Enter your age: "))

if age < 18:
    print("You are still a minor")
else:
    print("You are an adult")


#1.2
def diamondCreationFunc():
    while True:
        diamondHeight = int(input("Enter the desired height of your diamond (must be even): "))
        if diamondHeight % 2 == 0:
            break
        print("Please enter a correct even height value for a diamond.")

    midpoint = diamondHeight // 2

    for i in range(midpoint):
        spaces = " " * (midpoint - i)
        stars = "*" * (2 * i + 1)
        print(f"{spaces}{stars}{spaces}")

    for i in range(midpoint - 1, -1, -1):
        spaces = " " * (midpoint - i)
        stars = "*" * (2 * i + 1)
        print(f"{spaces}{stars}{spaces}")

diamondCreationFunc()
