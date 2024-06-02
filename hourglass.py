def hourglassSum(arr):
    hourglass = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            k = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass.append(k)
    return max(hourglass)


arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
result = hourglassSum(arr)
print(result)