def repeatedString(s, n):
    # Write your code here
    s_len = len(s)
    rem = n%s_len
    quo = n//s_len
    a_count = 0
    if rem == 0:
        a_count = s.count("a")*quo
    else:
        a_count = s.count("a")*quo + s[0:rem].count("a")
    return a_count


s = input()
n = int(input())
result = repeatedString(s, n)
print(result)
