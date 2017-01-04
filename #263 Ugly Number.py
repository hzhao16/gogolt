#263 Ugly Number
'''Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
Note that 1 is typically treated as an ugly number.
'''

'''
Keep dividing by 2,3,5
'''

def isUgly(self, a):
        """
        :type a: int
        :rtype: bool
        """
        if a <= 0:
            return False
        for i in [2,3,5]:
            while a%i==0:
                a = a/i
        return a==1