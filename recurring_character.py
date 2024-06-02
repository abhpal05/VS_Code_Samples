"""
Collections module implements specialized container datatypes providing alternatives to Python s general purpose built-in containers, dict, list, set, and tuple.
A Counter is a dict subclass for counting hashable objects. 
It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
Your task is to find the top two most recurring characters in a given string using most_common() function of the module.

Input Format
First line will contain a string s.

Constraints
1 <= |s| <= 10^3

Output Format
Output the two most recurring characters in the string along with their frequencies. 

"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from collections import Counter

def main(): 
    input_string = input() 
    count = Counter(input_string) 
    for q in count.most_common(2): 
        print(q, end=" ")


main()
