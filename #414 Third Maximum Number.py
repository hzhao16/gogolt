#414 Third Maximum Number
'''
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. The time complexity must be in O(n).
'''

# scan in one iteration
def thirdMax(nums):
    max1,max2,max3 = None,None,None
    for i in nums:
        if i==max1 or i==max2 or i==max3:
            continue
        if max1==None or i>max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif max2==None or i>max2:
            max3 = max2
            max2 = i
        elif max3==None or i>max3:
            max3 = i
        else:
            continue
    return max3 if max3!=None else max1

# remove max
def thirdMax1(nums):
    nums = set(nums)
    max1 = max(nums)
    if len(set(nums))<3:
        return max1
    nums.remove(max(nums))
    nums.remove(max(nums))
    max3 = max(nums)
    return max3
