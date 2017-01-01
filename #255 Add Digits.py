# 255 Add Digits
'''Given a non-negative integer num, 
repeatedly add all its digits until the result has only one digit.
'''
'''*** the one digit == n%9 *** '''
def addDigits(num):
    if num%9==0 and num!=0:
        return 9
    else:
        return num%9