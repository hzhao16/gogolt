#171 Excel Sheet Column Number
'''Given a column title as appear in an Excel sheet, 
return its corresponding column number.'''

def titleToNumber(s):
    n = len(s)
    col = 0
    for i in range(n):
        col+= (ord(s[i])-64)*(26**(n-i-1))
    return col

from functools import reduce
def titleToNumber_1(s):
    return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])

