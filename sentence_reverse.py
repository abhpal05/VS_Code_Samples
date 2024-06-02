# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order

# without function

from typing import Reversible


input_string = input("Enter your string :")

def reverse_sentense(lst):
    return [ele for ele in reversed(lst)]

main_list = input_string.split(" ")
result = " ".join(reverse_sentense(main_list))
print(result)

# with function
def sentence_Reverse(sntnce):
    input_list = sntnce.split(" ")
    result_sntnce = " ".join(Reversible(input_list))
    return result_sntnce

print(sentence_Reverse(input_string))
