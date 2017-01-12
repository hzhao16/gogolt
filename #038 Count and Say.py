#38. Count and Say  
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''


def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    if n==0:
        return ""
    s = '1'
    while n>=2:
        c = ""
        n = n-1
        i=0
        while i<len(s):
            count = 1
            while i<len(s)-1 and s[i]==s[i+1]:
                count+=1
                i+=1
            c += str(count)+s[i]
            i+=1
        s = c
    return s
