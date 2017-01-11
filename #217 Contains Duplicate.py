#217 Contains Duplicate

'''Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array,
 and it should return false if every element is distinct.
'''
# ***hash table**
def containsDuplicate(nums):
    n = len(nums)
    d = {}
    for i in range(n):
        if d.get(nums[i],None):
            return True  
        else:
            d[nums[i]] = 1
    return False

# set
def containsDuplicate_1(nums):
    return len(nums)!=len(set(nums))
