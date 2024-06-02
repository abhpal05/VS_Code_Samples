def sockMerchant(n, ar):
    # Write your code here
    s = set(ar)
    for item in ar:
        s.add(item)
    d = {}
    for sitem in s:
        d[sitem] = ar.count(sitem)
    p_count = 0
    for value in d.values():
        if(value > 1):
            p_count = p_count+ (value//2)
    return p_count


n = int(input())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)

    
