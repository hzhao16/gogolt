class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        tem = n
        num = 9
        l = 1
        start = 1
        while (tem - num*l > 0):
            tem -= num * l
            num *= 10
            start *= 10
            l += 1
        number = start + tem//l - 1
        if (tem % l == 0):
            return number % 10
        else:
            return int(str(number+1)[tem%l-1])