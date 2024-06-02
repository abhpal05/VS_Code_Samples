"""
String Concatenation (100 Marks)
You just need to take two strings as input from stdin and concatenate them and print the concatenated string to the stdout.

Input Format
You will be taking two strings as an input from stdin one on each line respectively.

Constraints
1 <= |S| <= 10000

Output Format
You need to print the concatenated string to the stdout.
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    s1 = input()
    s2 = input()
    s = s1.strip() + s2.strip()
    print(s)

 # Write code here 

main()

