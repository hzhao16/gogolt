import numpy as np
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        if A == []: return 0
        ans = [0] * len(A)
        l = list(range(len(A)))
        for i in range(len(A)):
            ans[i] = int(np.dot(l, A))
            A = [A[-1]] + A[0:-1]
        return max(ans)
        """
        if A == []: return 0
        n = len(A)
        l = list(range(n))
        ans = [0] * len(A)
        Sum = sum(A)
        ans[0] = int(np.dot(l, A))
        for i in range(1, n):
            ans[i] = ans[i-1] + Sum - n * A[n - i]
        return max(ans)