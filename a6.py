a = input("Pleasee enter a sentence: ")
b = input("Please enter a word: ")
if b in a :
    c = a.index(b)
    print(f"The word '{b}' exists in the sentence at index {c}.")
else:
    print(f"The word '{b}' does not exist in the sentence.")
    #Exercise 6: Substring Search
#Write a Python program that:
# 1. Asks for a sentence input from the user.
# 2. Asks for a word to search in the sentence.
# 3. Outputs whether the word exists in the sentence and, if it does, at which position (index).