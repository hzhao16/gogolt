#219 Contains Duplicate II

'''
Given an array of integers and an integer k, 
find out whether there are two distinct indices i and j in the array 
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''

# hash
def containsNearbyDuplicate(nums, k):
    n = len(nums)
    d = {}
    for i in range(n):
        if d.get(nums[i],None)!=None and i-d[nums[i]]<=k:
            return True
        d[nums[i]] = i            
    return False
