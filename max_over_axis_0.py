"""
Max of Min (100 Marks)
You will be given a 2-Dimensional Matrix of size NxM.
By using Inbuilt Max and Min function present in NumPy Package, You have to perform the min function over axis = 0 and then find the max of that.

Input Format
First line contains two integers N and M, denoting the size of the Matrix.
Next N lines contains M integers.

Constraints
2 <= N <= 100
2 <= M <= 100

Output Format
You have to print an Integer denoting the answer i.e  maximum over minimum(axis = 0).

Sample TestCase 1
Input
4 2
1 4
4 6
3 7
4 5
Output
4
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import numpy as np

def main():
    number_list = []
    n,m = input().split()
    n = int(n)
    m = int(m)
    for _ in range(n):
        line_input = list(map(int, input().rstrip().split()))
        number_list.append(line_input)
    number_array = np.asarray(number_list)
    max_value = np.amax(number_array, axis= 0)
    print(max_value[0])


main()


