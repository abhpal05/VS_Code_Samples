"""
Is your Number Armstrong? (100 Marks)
For this challenge, you need to take an integer input and store it in a variable of your choice and checks whether this number is an Armstrong number or not. 
If yes print 'True' else print 'False'.

Input Format
A single integer value to be taken as input from stdin and stored it in a variable. 

Constraints
1 < = n < = 18

Output Format
print 'True' if your number is Armstrong otherwise print 'False' to the stdout. 

Sample TestCase 1
Input
370
Output
True

"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import math as m

def main():
    n = int(input())
    n1 = 0
    n2 = n
    while(n>0):
        n1 = n1 + m.pow((n%10), 3)
        n = n//10
    if(n1==n2):
        print("True")
    else:
        print("False")

main()

