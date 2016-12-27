import re
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (s == "" or s.replace(" ",  "") == ""): return 0  
        ans = 0
        s = re.sub('\s+', " ", s)
        if (s[0] == " "):
            s = s[1:]
        if (s[-1] == " "):
            s = s[:-2]
        for i in s:
            if (i == " "):
                ans += 1
        return ans+1