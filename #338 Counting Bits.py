#338 Counting Bits

'''Given a non negative integer number num. 
For every numbers i in the range 0 ≤ i ≤ num 
calculate the number of 1's in their binary representation and return them as an array.
'''

'''The first n-1 digits of x is the same with x>>1, run recursively'''
def countBits(num):
    ans = [0]
    for x in range(1, num + 1):
        ans.append(ans[x >> 1] + (x & 1))
    return ans