class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d1 = collections.defaultdict(int)
        n = len(A)
        ans = 0
        for i in range(n):
            for j in range(n):
                d1[A[i] + B[j]] += 1

        for i in range(n):
            for j in range(n):
                target = -1 * (C[i] + D[j])
                ans += d1[target]
        return ans