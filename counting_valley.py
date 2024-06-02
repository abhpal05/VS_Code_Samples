def countingValleys(steps, path):
    h = 0
    valley_count = 0
    for i in range(steps):
        if(path[i] == "U"):
            h = h+1
        if(path[i] == "D"):
            h = h-1
        if((h==0) and (path[i]=="U")):
            valley_count = valley_count + 1
    return valley_count




step = int(input().strip())
path = input()
result = countingValleys(step, path)
print(result)