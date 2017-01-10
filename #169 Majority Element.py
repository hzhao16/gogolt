#169 Majority Element
'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
'''

#***dict***#
def majorityElement(nums):
    n = len(nums)
    d = {}
    for i in range(n):
        d[nums[i]]=d.get(nums[i],0)+1
        if d[nums[i]]> int(n/2):
            return nums[i] 

#count
def majorityElement1(nums):
    n = len(nums)
    major = nums[0]
    count = 1
    for i in range(1,n):
        if not count:
            count+=1
            major = nums[i]
        elif major == nums[i]:
            count+=1
        else:
            count-=1
    return major
