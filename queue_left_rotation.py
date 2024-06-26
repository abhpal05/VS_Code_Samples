"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], 
then the array would become [3,4,5,1,2]. Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
"""


def rotLeft(a, d):
    # Write your code here
    for _ in range(d):
        a.append(a.pop(0))
    return a

multiple_input = input().strip().split()
n = int(multiple_input[0])
d = int(multiple_input[1])
a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)
print(' '.join(map(str, result)))