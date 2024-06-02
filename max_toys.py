"""
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. 
There are a number of different toys lying in front of him, tagged with their prices. 
Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. 
Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

Note Each toy can be purchased only once.
"""

def maximumToys(prices, k):
    # Write your code here
    sum = 0
    count = 0
    prices_sorted = sorted(prices)
    for i in range(len(prices_sorted)):
        if (sum <= k):
            sum = sum + prices_sorted[i]
            count = count + 1
    return count-1


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
prices = list(map(int, input().rstrip().split()))
result = maximumToys(prices, k)
print(str(result) + '\n')