class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i, start= 0, 0
        ans = []
        while (i < len(nums)):
            if nums[i] + 1 in nums:
                i += 1
                continue
            else:
                if (start < i):
                    ans.append(str(nums[start]) + "->" + str(nums[i]))
                else:
                    ans.append(str(nums[start]))
                start = i + 1
            i += 1
        return ans