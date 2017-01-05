#67 Add Binary

'''Given two binary strings, return their sum (also a binary string).'''

'''***Similar to #415***'''
def addBinary(num1, num2):
    n1 = len(num1)
    n2 = len(num2)
    i = n1-1
    j = n2-1
    s = []
    c = 0
    while i>=0 or j>=0 or c==1:
        x = ord(num1[i])-ord('0') if i>=0 else 0
        y = ord(num2[j])-ord('0') if j>=0 else 0
        s.append((x+y+c)%2)
        c = int((x+y+c)/2)
        i-=1
        j-=1
    return ''.join(str(i) for i in s[::-1])


'''Recursive way'''
def addBinary_1(a, b):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
        
    if len(a)==0: return b
    if len(b)==0: return a
    if a[-1] == '1' and b[-1] == '1':
        return addBinary(addBinary(a[0:-1],b[0:-1]),'1')+'0'
    if a[-1] == '0' and b[-1] == '0':
        return addBinary(a[0:-1],b[0:-1])+'0'
    else:
        return addBinary(a[0:-1],b[0:-1])+'1'

        