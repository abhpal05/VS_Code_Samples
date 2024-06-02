"""
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
You are allowed to swap any two elements. Find the minimum number of swaps required to list_sort the array in ascending order.

"""

def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swaps = swaps+1
    print("Array is sorted in " + str(swaps) + " swaps.")
    print("First Element: " + str(arr[0]))
    print("Last Element: " + str(arr[n-1])) 


n = int(input())
arr = list(map(int, input().rstrip().split()))
res = minimumSwaps(arr)
print(str(res) + '\n')