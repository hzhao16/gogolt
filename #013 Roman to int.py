#13 Roman to int

'''Given a roman numeral, convert it to an integer.'''

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """ 
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    a = 0
    n = len(s)
    for i in range(n):
        if i < n-1 and roman[s[i]] < roman[s[i+1]]:
            a = a - roman[s[i]]
        else:
            a = a + roman[s[i]]
    return a
