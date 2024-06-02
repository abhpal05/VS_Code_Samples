"""

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false

"""

import math as ma

# If number is greater than 10, then square of digits of the number are added
def sumSquare(j) -> int:
    k = 0
    while(j != 0):
        k = k + int(ma.pow((j%10),2))
        j = j//10
    return k

def happyNum(n) -> bool:
    while(n>=10):
        n = sumSquare(n)
    if(n==1):
        return True
    else:
        return False


n = input("Enter Number: ")
print(happyNum(int(n)))