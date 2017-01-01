# 122 Best Time to Buy and Sell Stock II
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).
'''

''' capture every uptick'''

def maxProfit(prices):
    n = len(prices)
    l = [prices[i]-prices[i-1] for i in range(1,n)]
    sum = 0
    for i in range(len(l)):
        if l[i]>0:
            sum += l[i]
    return sum
prices = [7, 1, 5, 3, 6, 4]
maxProfit(prices)