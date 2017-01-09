#283 Move Zeroes
'''
Given an array nums, 
write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, 
nums should be [1, 3, 12, 0, 0].
'''

'''***move non-zero elements forward and fill rest with 0s'''

def moveZeroes(nums):
    n = len(nums)
    c = -1
    for i in range(n):
        if nums[i]:
            c+=1
            nums[c] = nums[i]
    while c<n-1:
        nums[c+1]=0
        c += 1
    return nums