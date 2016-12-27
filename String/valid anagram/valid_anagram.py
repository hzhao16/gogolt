class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if j in d:
                d[j] -= 1
            else:
                return False
        for i in d:
            if (d[i] != 0):
                return False
        return True 