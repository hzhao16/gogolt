#27 Remove Element
'''
Given an array and a value, 
remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, 
you must do this in place with constant memory.
The order of elements can be changed. 
It doesn't matter what you leave beyond the new length.
'''

'''***move forward***'''

def removeElement(nums, val):
    n = len(nums)
    c = 0
    for i in range(n):
        if nums[i]!=val:
            c+=1
            nums[c-1]=nums[i]
    return c

