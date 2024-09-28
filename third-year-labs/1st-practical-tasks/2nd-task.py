from collections import Counter

# 2.Strings
""" 2.1 The user enters a sentence. Write a program that outputs this sentence
backwards (not words, but sentence symbols). """
user_sentence_input = input("Please enter some text: ")


def print_reversed_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    print("Here are the words you entered in reverse order:" +
          " ".join(reversed_words))
    return


print_reversed_words(user_sentence_input)
""" 2.2 The user enters a word. Write a program that outputs
the letter that occurs most often in the word and the number of its occurrences.
(Hint: Use the key argument for the max() function) """
user_word_input = input("Please enter a word: ")


def find_most_frequent_letter(word):
    most_common = Counter(word).most_common(1)[0]
    return most_common


most_frequent_letter, number_of_occurrences = find_most_frequent_letter(
    user_word_input)

print(
    f"The most frequent letter in the word you entered is: {most_frequent_letter} "
    f"And the number of occurrences is: {number_of_occurrences}")
 