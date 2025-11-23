# Write a python program that takes any word or sentene as input and prints:
# The first character
# The last character
# the total number of characters

message = input("Enter a word or sentence: ")  # message - "Clouds drift slowly, carrying dreams across endless skies of wonder."

first_character = message[0]
print("First character::", first_character)  # first character

last_character = message[-1]
print("Last character::", last_character)  # last character

total_characters = len(message)
print("Total number of characters::", total_characters)  # total number of characters
