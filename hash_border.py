"""
Problem
You are given a table with n rows and m columns. 
Each cell is colored with white or black. Considering the shapes created by black cells, what is the maximum border of these shapes?

A shape is a set of connected cells. Two cells are connected if they share an edge. Note that no shape has a hole in it.

Input format

The first line contains t denoting the number of test cases.
The first line of each test case contains integers n,m denoting the number of rows and columns of the matrix. 
Here, '#' represents a black cell and '.' represents a white cell. 
Each of the next  lines contains  integers.
"""

test_case = int(input())

for i in range(test_case):
    r,c = input().split()
    r = int(r)
    c = int(c)
    border_list = []
    for j in range(r):
        r_input = input()
        hash_count = 0
        for k in range(c):
            if r_input[k] == "#":
                hash_count = hash_count + 1
        border_list.append(hash_count)
    print(max(border_list))

