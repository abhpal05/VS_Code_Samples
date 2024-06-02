"""
Count special numbers between boundaries (100 Marks)
For this challenge, you are given a range and you need to find how many prime numbers lying between the given range.

Input Format
For this challenge, you need to take two integers on separate lines. These numbers defines the range. 

Constraints
1 < = ( a , b ) < = 100000

Output Format
output will be the single number which tells how many prime numbers are there between given range.
Sample TestCase 1
Input
1
20
Output
8

"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def get_prime_number(n):
    for a in range(2, ((n//2)+1)):
        if(n%a == 0):
            return 0
    return 1

def main():
    prime_count = 0
    x = int(input())
    y = int(input())
    for i in range(x, y):
        check = get_prime_number(i)
        if(check == 1) and (i!=1):
            prime_count = prime_count + 1
    print(prime_count)


main()

