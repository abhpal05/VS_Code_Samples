"""
Decide yourself with conditional statement (100 Marks)
For this challenge, you need to read a integer value(default name - age) from stdin, store it in a variable and then compare that value with the conditions given below -
    - if age is less than 10, then print 'I am happy as having no responsibilities.' to the stdout.
    - if age is equal to or greater than 10 but less than 18, then print 'I am still happy but starts feeling pressure of life.' to the stdout.
    - if age is equal to or greater than 18, then print 'I am very much happy as i handled the pressure very well.' to the stdout. 

Input Format
A single line to be taken as input and save it into a variable of your choice(Default name - age). 

Constraints
1 < = age < = 100 

Output Format
Print the sentence according to the value of the integer which you had taken as an input. 

Sample TestCase 1
Input
8
Output
I am happy as having no responsibilities.

"""

def main():
    age = int(input())
    if(age<10):
        print("I am happy as having no responsibilities.")
    elif((age>=10) and (age<18)):
        print("I am still happy but starts feeling pressure of life.")
    else:
        print("I am very much happy as i handled the pressure very well.")

main()
