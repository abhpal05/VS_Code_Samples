#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    # Write your code here
    vowels = "aeiou"
    substring_dictonary = {}
    for i in range(0, len(s)-k):
        substring = s[i: (i+k)]
        vowel_count = [substring.count(x) for x in vowels]
        substring_dictonary[substring] = sum(vowel_count)
    
    answer =max(zip(substring_dictonary.values(), substring_dictonary.keys()))[1]
    return answer
        
        

if __name__ == '__main__':

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    print(result)
