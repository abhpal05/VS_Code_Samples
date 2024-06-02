"""
Third Largest (100 Marks)
You will be given an array and you need to find the third largest and print it to the stdout.

Note: The length of the array should not be less than 3.

Input Format
You will be taking a number as an input stdin which tells about the length of the array. On another line, array elements should be there with single space between them.

Constraints
1 <= L <= 1000
1 <= Ai <= 1000

Output Format
You need to print the third largest element to the stdout.

Sample TestCase 1
Input
7
25 26 7 8 10 11 79
Output
25

"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    test_case=int(input())
    number_list= list(map(int,  input().rstrip().split()))
    number_list.sort(reverse=True)
    print(number_list[2])

main()

