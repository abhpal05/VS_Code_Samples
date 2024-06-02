"""
Validate Debit Card (100 Marks)
Debit Cards Validation is an important step in E- Commerce. Using Regex on the Client Side itself, once can reduce the load on the server.
Here, we have few Debit Card Numbers with us. You have to output "Valid" for a Valid Debit Card, "Invalid" for a Invalid Debit Card.
Valid Debit Cards have following properties : 
It must start with a 7, 8 or 9. 
It must contain exactly  digits 16 digits. 
It may have digits in groups of 4, separated by one hyphen "-". 

Input Format
First line will contain an Integer, denoting the number of Debit  Cards to validate.
Each of the next N lines will contain a string denoting the Debit Card Number.

Constraints
1 <= N <= 50

Output Format
Output a string "Valid" if the given Debit Card is Valid, otherwise print "Invalid".

Sample TestCase 1
Input
3
1234421312224231
7293-3124-5232-4231
7982214254367642
Output
Invalid
Valid
Valid

"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    card_number_list = []
    test_Case = int(input())
    for _ in range(test_Case):
        card_number_list.append(input())
    for i in range(test_Case):
        card_number = card_number_list[i]
        card_number = card_number.replace("-","")
        if(len(card_number) != 16):
            print("Invalid")
        elif((card_number[0] == "7") or (card_number[0] == "8") or (card_number[0] == "9")):
            print("Valid")
        else:
            print("Invalid")

main()

