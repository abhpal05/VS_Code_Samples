"""
Reshape The Array (100 Marks)
The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array. 
The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.
Now, Given 9 Integers, You have to convert them into 3*3 Numpy array using Reshape function.

Input Format
Single line containing 9 space separated integers.

Constraints
1 <= Integers <= 100

Output Format
Output 3*3 Numpy Array.

Sample TestCase 1
Input
1 2 3 4 5 6 7 8 9
Output
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import numpy as np

def main():
    number_list = list(map(int, input().rstrip().split()))
    print(np.reshape(number_list, (3,3)))

main()
