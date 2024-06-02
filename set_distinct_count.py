"""
Managing Bank (100 Marks)
You are working as a Manager in a bank. At the end of the day, You have to send a report to your supervisors which consists of count of distinct accounts that were operated upon on that particular day.
You are given a list containing the account numbers of the customers of the bank according to their time of arrival in the bank.
You have to tell the count of distinct accounts.

Input Format
First line will contain N, denoting the total number of entries in the list.
Next line will contain N account numbers separated by space.

Constraints
1 <= N <= 10^3
1 <= Account Number <= 10^2

Output Format
Output the count of distinct accounts for a particular day.

"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    # Write code here
    n = int(input())
    b = input()
    set1 = set(int(x) for x in b.split())
    print(len(set1)) 

main()
