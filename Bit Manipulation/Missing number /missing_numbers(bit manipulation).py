class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return sum(list(range(len(nums)+1))) - sum(nums)
        ans = 0
        for i in range(len(nums)):
            ans ^= (i+1) ^ nums[i]
        return ans