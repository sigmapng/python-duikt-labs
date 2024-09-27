# Strings

#2.1
sentence = input("Enter your sentence, please: ")

reversedSentence = sentence[::-1]
print("There's your sentence reverced:", reversedSentence)

#2.2
word = input("Enter a word, please: ").lower()

letterCount = {}

for letter in word:
    if letter in letterCount:
        letterCount[letter] += 1
    else:
        letterCount[letter] = 1

mostCommonLetter = max(letterCount, key=letterCount.get)
count = letterCount[mostCommonLetter]

print(f"Most common letter: {mostCommonLetter}")
print(f"Number of occurrences: {count}")
