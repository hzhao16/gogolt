# 121 Best Time to Buy and Sell Stock 

''' Say you have an array for which the ith element 
is the price of a given stock on day i.
design an algorithm to find the maximum profit.'''

''' *** same with finding max sum subarray ***'''

def maxProfit(self, prices):
    n = len(prices)
    l = [prices[i]-prices[i-1] for i in range(1,n)]
    sum = 0
    max = 0
    for i in range(len(l)):
        sum += l[i]
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0
    return max