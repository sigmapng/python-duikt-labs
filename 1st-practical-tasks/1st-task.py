# Dictionary to store user inputs
userData = {
    "What is your name? ": "Your name is",
    "How old are you? ": "You are",
    "Where do you live? ": "You live in",
    "Where do you study? ": "You study at",
    "What is the number of your group? ": "Your group number is",
    "What is your number in the list of the students? ": "Your list number is",
    "What was your ZNO results in Ukrainian? ": "Your result was",
    "Are you planning on getting master degree? ": "Masters degree",
}

# Collect user inputs
userInputs = {question: input(question) for question in userData.keys()}

# Print user data
for question, label in userData.items():
    print(f"{label}: {userInputs[question]}")
