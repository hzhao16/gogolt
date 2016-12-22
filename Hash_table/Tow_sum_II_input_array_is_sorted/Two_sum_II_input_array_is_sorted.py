class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(numbers):
            d[i] = target - n
            if (i >= 1 and d[i] == d[i-1]):
                continue
            else:
                if ((target - n) in numbers):
                    if (numbers.index(target- n) == i):
                        return [i+1,i+2]
                    return [i+1, numbers.index(target- n)+1]