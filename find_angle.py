''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
import math

def main():
    adjacent=int(input())
    opposite=int(input())
    #since tan=opposite/adjacent
    tangent=opposite/adjacent
    sys.stdout.write(str(int(math.degrees(math.atan(tangent)))))

 # Write code here 

main()

