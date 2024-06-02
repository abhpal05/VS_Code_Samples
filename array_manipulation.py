"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. 
Once all operations have been performed, return the maximum value in the array.

"""

from collections import Counter

def arrayManipulation(n, queries):
    # Write your code here
    input_array = []
    for _ in range(n):
        input_array.append(0)
    for j in range(len(queries)):
        for k in range((queries[j][0]-1), (queries[j][1])):
            input_array[k] = input_array[k] + queries[j][2]
    max_array = max(input_array)
    return max_array

# def arrayManipulation(n, queries):
#     c = Counter()
#     for a,b,k in queries:
#         c[a] += k
#         c[b+1] -= k
#     arrSum = 0
#     maxSum = 0
#     for i in sorted(c)[:-1]:
#         arrSum += c[i]
#         maxSum = max(arrSum, maxSum)
#     return maxSum



first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
queries = []
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
# print(queries)
# for i in range(len(queries)):
#     print(str(queries[i][0]), end=" ")
result = arrayManipulation(n, queries)
print(str(result) + '\n')