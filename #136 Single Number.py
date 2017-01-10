#136 Single Number

'''
Given an array of integers, 
every element appears twice except for one. Find that single one.

'''

# *** dict
def singleNumber(nums):
    n = len(nums)
    d = {}
    for i in range(n):
        d[nums[i]]=d.get(nums[i],0)+1
    for k,v in d.items():
        if v==1:
            return k

# XOR -> x^x = 0, 0^x = x 
def singleNumber1(nums):
    result = 0
    for i in nums:
        result ^= i
    return result
