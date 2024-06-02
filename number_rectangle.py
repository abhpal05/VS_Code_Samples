"""
You need to take an integer input and then draw the pattern according to it. Say for example if you enter 5 then, the pattern should be like this-
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    # Write code here 
    n = int(input())
    i = 1
    for i in range(1, n+1):
        number_list = []
        for j in range(1, n+1):
            number_list.append(i)
        print(*number_list, sep = " ")


main()

