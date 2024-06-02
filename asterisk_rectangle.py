'''
You need to take an integer input and then draw the pattern according to it. 
Say for example if you enter 6 then, the pattern should be like this- 
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * * 
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT



def main():
    # Write code here 
    n = int(input())
    for i  in range(1, n+1):
        as_list = []
        for j in range(1, n):
            as_list.append("*")
        print(*as_list, sep= " ")


main()

