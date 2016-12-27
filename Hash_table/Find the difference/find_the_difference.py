class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d1 = collections.Counter(s)
        d2 = collections.Counter(t)
        for key, value in d2.items():
            if (key not in d1.keys() or value != d1[key]):
                return key