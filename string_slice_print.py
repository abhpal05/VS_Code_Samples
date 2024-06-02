"""
Print Exact Slice Of String (100 Marks)
You need to take string input and two other numbers which will be the start and end point of the slice and you need to print that slice of string to the stdout.

Input Format
You will be taking a string as an input from stdin and two integers one on each line.

Constraints
1 <= |S| <= 10000

Output Format
You need to print the slice of the string to the stdout.
"""


''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    # Write code here 
    input_string = input()
    a = int(input())
    b = int(input())
    print(input_string[a:(b+1)])

main()

