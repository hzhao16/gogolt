class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (nums[abs(nums[i]) - 1] > 0):
                nums[abs(nums[i]) - 1] = - nums[abs(nums[i]) - 1]
        ans = []        
        for i in range(len(nums)):
            if (nums[i] > 0):
                ans.append(i+1)
        return ans