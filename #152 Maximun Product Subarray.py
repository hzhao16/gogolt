# 152 Maximum Product Subarray
'''Find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

Returns max product as well as the subarray
'''

def maxpro(nums):
    nmax = nums[0]
    nmin = nums[0]
    gmax = nums[0]
    start, end = 0,0
    n = len(nums)
    for i in range(1,n):
        if nums[i]<0:
            nmax,nmin = nmin,nmax
        nmax = max(nums[i], nmax*nums[i])
        nmin = min(nums[i], nmin*nums[i])
        if gmax < nmax:
            end = i
        gmax = max(gmax, nmax)
        print(nmax, nmin, gmax, end)
    temp = gmax
    start = end
    while temp!=1:
        temp = temp/nums[start]
        start -= 1
    print(nums[start+1:end+1])
    return gmax