"""
Validate Email Address (100 Marks)
During the process of information gathering, we have to make sure that it is valid. Regex comes very handy in such tasks.
Here, we have few email addresses with us. You have to output only the valid email address.
Valid email addresses are composed of a username, domain name, and extension assembled in this format: username@domain.extension.
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is , , or  characters in length.

Input Format
First line will contain an Integer, denoting the number of emails to validate.
Each of the next N lines will contain a string denoting the email address.

Constraints
1 <= N <= 50

Output Format
Output all the valid email address.

Sample TestCase 1
Input
2
harsh.chauhan@gmail.com
test@in
Output
harsh.chauhan@gmail.com
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import re

def main():
    email_list = []
    email_pattern = r".+.@.+.com"
    test_case = int(input())
    for _ in range(test_case):
        email_list.append(input())
    for i in range(test_case):
        if re.match(email_pattern, email_list[i]):
            print(email_list[i])
    

 # Write code here 

main()