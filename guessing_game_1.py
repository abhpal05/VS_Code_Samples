# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

import random
a = random.randint(1,9)
#print(a)

input_number = int(input("Enter a number: "))
if(input_number == a):
    print("You guessed right")
elif(input_number > a):
    print("You guessed higher")
else:
    print("You guessed lower.")
 
 