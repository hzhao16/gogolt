#26 Remove Duplicates from Sorted Array

'''
Given a sorted array, 
remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.

'''

'''***move forward***'''

def removeDuplicates(nums):
    n = len(nums)
    if n==0:
        return n
    c = 0
    for i in range(1,n):
        if nums[i]>=nums[c]:
            c+=1
            nums[c]=nums[i]
    return c+1