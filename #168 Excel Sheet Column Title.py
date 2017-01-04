#168. Excel Sheet Column Title

'''Given a positive integer, 
return its corresponding column title as appear in an Excel sheet.
'''

''' (n-1)%26 '''
def convertToTitle(n):
    s = []
    while n>0:
        d,n = (n-1)%26, int((n-1)/26)
        s.append(d)
    L = ''.join(chr(i+65) for i in reversed(s))
    return L

