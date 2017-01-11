#349 Intersection of Two Arrays
'''
Given two arrays, write a function to compute their intersection.

'''

def intersection(nums1, nums2):
    return list(set([i for i in nums1 if i in nums2]))

def intersection1(nums1,nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    return list(nums1&nums2)