"""
Validate Phone Numbers (100 Marks)
In the country of Utopia, Phones Numbers starts with the digit 1 or 2 followed by exactly 12 digits i.e Phones Numbers comprises of 13 digits.
Now, Given N numbers you have to check, whether they are Valid or Invalid.
If they are Valid, print Valid" otherwise print "Invalid".

Input Format
First Line will contain an Integer, denoting the count of phone numbers.
Each of the Next N lines, contains a Phone Number.

Constraints
1 <= N <= 10^3

Output Format
For each Phone Number, print "Valid" or "Invalid" in a new line.
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    sample_phone_number_list = []
    test_Case = int(input())
    for _ in range(test_Case):
        sample_phone_number_list.append(input())
    for i in range(test_Case):
        sample_phone_number = sample_phone_number_list[i]
        if(len(sample_phone_number) != 13):
            print("Invalid")
        elif((sample_phone_number[0] == "1") or (sample_phone_number[0] == "2")):
            print("Valid")
        else:
            print("Invalid")

main()
