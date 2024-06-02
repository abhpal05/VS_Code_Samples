"""
String Membership (100 Marks)
You just need to take string and a character as an input from stdin and print 'True' if that character is present in that string otherwise print 'False'.

Input Format
You will be taking a string and a character as an input from stdin.

Constraints
1 <= |S| <= 10000

Output Format
Print 'True' if that character is present in that string otherwise print 'False'.
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    # Write code here 
    input_string = input().upper()
    input_char = input().upper()
    for element in input_string:
        if element == input_char:
            print("True")
            return
    print("False")

main()