''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def fib(number):
    if number <= 1:
        return number
    else:
        return (fib(number - 1) + fib(number - 2))

def main():
    # Write code here
    n = int(input())
    fib_list = []
    for i in range(n):
        fib_list.append(fib(i))
    print(*fib_list, sep=" ")

main()