#326 power of 3

'''Given an integer (signed 32 bits), write a function to check whether it is a power of 3.'''

import math

def ispower3_1(num):
    if num<=0:
        return False
    while (num!=1):
        if num%3 != 0:
            return False
        num = num/3
    return True

def ispower3_2(num):
    if num<=0:
        return False
    maxnum = 3**int((math.log(2**31-1)/math.log(3)))
    return maxnum%num==0

def ispower3_3(num):
    if num<=0:
        return False
    t = math.log(num)/math.log(3)
    return abs(math.ceil(t)-t)<=10**-10

def ispower3_4(num):
    if num<=0:
        return False
    t = math.log(num,3)
    return abs(math.ceil(t)-t)<=10**-10