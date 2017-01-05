# 53 Maximum Subarray
'''Find the contiguous subarray within an array (containing at least one number) 
which has the largest sum.

Returns max sum as well as the subarray

'''

import sys
def maxsub(nums):
    max = -sys.maxsize-1
    sum = 0
    start = 0
    n = len(nums)
    end = 0
    for i in range(n):
        sum += nums[i]
        if sum > max:
            max = sum
            end = i
        if sum < 0:
            sum = 0
            start = i
        print(sum, max, start, end)
    if start > end:
        print(nums[:end+1])
    else:
        print(nums[start+1:end+1]) 
    return max
