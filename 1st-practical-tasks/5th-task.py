numList = []

for i in range(3):
    numList.append(int(input(f"Enter {i+1} Number: ")))

numList.sort()
minValue = min(numList)
maxValue = max(numList)

print("\nMinimal value is:", minValue)
print("Maximum value is:", maxValue)
