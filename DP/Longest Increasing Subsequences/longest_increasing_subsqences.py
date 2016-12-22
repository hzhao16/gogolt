class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [1] * len(nums)
        ans = 0
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if (nums[i] > nums[j]):
                    l[i] = max(l[i], l[j]+1)
            ans = max(ans, l[i])
        return ans   