#441 Arranging Coins

'''
You have a total of n coins that you want to form in a staircase shape, 
where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.
'''

'''*** loop'''
def arrangeCoins(n):
    i = 1
    c = 0
    while n>=i:
        n = n-i
        c +=1
        i += 1
    return c

'''solve k^2+k-2n=0 directly'''
def arrangeCoins_1(n):
    return int(int((1+8*n)**0.5-1)/2)
