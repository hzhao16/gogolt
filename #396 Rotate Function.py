#396. Rotate Function
'''Given an array of integers A and let n to be its length.
Assume Bk to be an array obtained by rotating the array A k positions clock-wise, 
we define a "rotation function" F on A as follow:
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
Calculate the maximum value of F(0), F(1), ..., F(n-1).
'''

'''
F(k) - F(k-1) = Bk[1] + Bk[2] + ... + Bk[n-1] + (1-n)Bk[0]
              = (Bk[0] + ... + Bk[n-1]) - nBk[0]
              = sum - nBk[0]
'''

def maxRotateFunction(A):
    s = sum(A)
    n = len(A)
    F = sum([A[i]*i for i in range(n)])
    maxF = F
    for i in range(1,n):
        F = F+s-n*A[n-i]
        maxF = max(F,maxF)
    return maxF