def jumpingOnClouds(c):
    # Write your code here
    jump = 0
    for i in range(len(c)):
        if((c[i+1] != 1) or (c[i+2] == 0)) and ((i+2)<len(c)):
            i = i+2
            jump = jump + 1
        elif((i+1)<len(c)):
            jump = jump+1
    return jump



n = int(input())
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c)
print(result)


