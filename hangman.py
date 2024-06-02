"""
This exercise is Part 1 of 3 of the Hangman exercise series. 
The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
 Download this file and save it in the same directory as your Python code. 
 This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. 
 Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.

"""

import random

# Create empty list
word_list = []

# Read the file
with open('sowpods.txt', 'r') as f:
    line = f.readline().strip()
    word_list.append(line)
    while line:
        line = f.readline().strip()
        word_list.append(line)

# Generate random number
random_number = random.randint(0, len(word_list))

# Print random word
# print("Random Word from txt is: ", word_list[random_number])

random_word = word_list[random_number]
random_word = random_word.upper()
