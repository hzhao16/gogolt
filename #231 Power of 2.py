#231 Power of 2
'''Given an integer, write a function to determine if it is a power of two.'''

'''Bit manipulation'''

def ispower2(num):
    if num<=0:
        return False
    return num&(num-1)==0


def My_ispower2(num):
    if num<=0:
        return False
    while(num!=1):
        if num%2 != 0:
            return False
        num = num>>1
    return True