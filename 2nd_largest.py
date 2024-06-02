"""
Who's the second largest? (100 Marks)
For this challenge, you need to take number of elements as input on one line and array elements as an input on another line 
and find the second largest array element and print that element to the stdout.

Input Format
In this challenge, you will take number of elements as input on one line and array elements which are space separated as input on another line. 

Constraints
1 < = n < = 100000
1 < = a[i] < = 10^9

Output Format
You will print the second largest element to the stdout. 

Sample TestCase 1
Input
6
11 22 33 44 55 66
Output
55

"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    number_count = int(input())
    number_list = list(map(int, input().rstrip().split()))
    number_list.remove(max(number_list))
    print(max(number_list))
    print(number_list)
main()