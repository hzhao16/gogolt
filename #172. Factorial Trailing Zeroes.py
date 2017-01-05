#172. Factorial Trailing Zeroes

'''Given an integer n, return the number of trailing zeroes in n!'''

'''***Count total number of factor 5***'''
def trailingZeroes(n):
    count = 0
    while n>1:
        count+=int(n/5)
        n = n/5
    return count

'''An recursive way, slower'''
def trailingZeroes_r(n):
    return 0 if n == 0 else n / 5 + trailingZeroes_r(n / 5)

