class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            
            if (num * 10 <= n):
                num = num * 10
            else:
                if (num >= n):
                    num = num / 10
                num += 1
                while (num % 10 == 0):
                    num /= 10
        return ans