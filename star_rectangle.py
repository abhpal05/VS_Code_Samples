def main():
    # Write code here 
    n = int(input())
    for _ in range(1, n+1):
        as_list = []
        for j in range(1, n):
            as_list.append("*")
        print(*as_list, sep= " ")


main()