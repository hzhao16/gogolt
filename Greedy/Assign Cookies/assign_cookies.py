class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        i, j = 0, 0
        while (i < len(g) and j < len(s)):
            if (g[i] <= s[j]):
                i += 1
                j += 1
                ans += 1
            elif (g[i] > s[j] and j < len(s)):
                j += 1
            elif (g[i] > s[j]): 
                break
        return ans