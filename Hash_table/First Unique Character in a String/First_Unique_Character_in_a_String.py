import operator
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return -1
        table = collections.Counter(s)
        d = {}
        for key, value in table.items():
            if (value == 1):
                d[key] = 1
        if not d: return -1 
        for key, value in d.items():
            d[key] = s.find(key)
        return d[min(d, key=d.get)]