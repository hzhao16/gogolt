#1 Two Sum
'''
Given an array of integers, 
return indices of the two numbers such that they add up to a specific target.
'''

# hash
def twoSum(nums, target):
	d = {}
	for i in range(len(nums)):
		if d.get(target-nums[i],None)==None:
			d[nums[i]]=i
		else:
			return [d[target-nums[i]],i]
