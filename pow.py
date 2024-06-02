''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import math

def main():
    # Write code here
    input_string = input()
    a,b,c = input_string.split()
    print(int(math.pow(int(a), int(b))%int(c)))


main()

