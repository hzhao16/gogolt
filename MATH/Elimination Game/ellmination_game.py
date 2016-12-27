class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [x + 1 for x in range(n)]
        sign = 1
        while (len(l) > 1):
            if (sign == 1):
                sign = 0
                i = 0
                tem = [i]
                while (i < len(l)):
                    i += 2
                    tem.append(i)
            elif (sign == 0):
                sign = 1
                i = len(l) - 1
                tem = [i]
                while (i >= 0):
                    i -= 2
                    tem.append(i)
            l = [v for i, v in enumerate(l) if i not in tem]
        return int(l[0])