# 415. Add Strings
'''Given two non-negative numbers num1 and num2 represented as string, 
return the sum of num1 and num2.'''

'''You must not use any built-in BigInteger library or convert the inputs to integer directly.'''

def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
    n1 = len(num1)
    n2 = len(num2)
    i = n1-1
    j = n2-1
    s = []
    c = 0
    while i>=0 or j>=0 or c==1:
        x = ord(num1[i])-ord('0') if i>=0 else 0
        y = ord(num2[j])-ord('0') if j>=0 else 0
        s.append((x+y+c)%10)
        c = int((x+y+c)/10)
        i-=1
        j-=1
    return ''.join(str(i) for i in s[::-1])