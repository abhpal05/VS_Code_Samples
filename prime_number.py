''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def check_prime(n):
    for x in range(2, ((n//2)+1)):
        if(n%x == 0):
            return
    print(n)

def main():
    min_n = int(input())
    max_n = int(input())
    for x in range(min_n, max_n+1):
        check_prime(x)

 # Write code here 

main()

