# Amazon BI question

# Problem 1
# Given a list find maximum occurance of a number
sample_list = [1,3,5,6,6,7,8,7,7,7,9,9,10,1]
max_occurance = max(sample_list, key = sample_list.count)
print(max_occurance)

# Problem 2
# Problem: Password is like 123abhc321, encrypt it like 321abc123
# Input: 
# 1. Interger (number of integers before and after char)
# 2. The password itself
sample_str = '123abn321'
n = 3

# Function to reverse number
def number_reverse(number_input):
    result_number = 0
    while(number_input > 0):
        result_number = (10*result_number) + (number_input%10)
        number_input = number_input//10
    return result_number

# Extract number part from input password (in string)
num =''
for c in sample_str:
    if c.isdigit():
        num = num+c
#print(num)

# Extract character part from password
input_char =''
for d in sample_str:
    if d.isalpha():
        input_char = ''.join([input_char, d])

# Split the number part into two different number, using input integer
num1 = int(num)//(10**n)
num2 = int(num)%(10**n)

# reverse the numbers using defined function
rev_num1 = number_reverse(num1)
rev_num2 = number_reverse(num2)

# output
print(str(rev_num1)+input_char+str(rev_num2))


