#242 Valid Anagram
'''
Given two strings s and t, write a function to determine if t is an anagram of s.
For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
'''

# ***dict/counter***
def isAnagram(s, t):
    from collections import Counter
    return Counter(t)==Counter(s)

def isAnagram1(s,t):
    d1,d2={},{}
    for i in s:
        d1[i] = d1.get(i,0)+1
    for i in t:
        d2[i] = d2.get(i,0)+1
    return d1==d2

# sort
def isAnagram2(s,t):
    return sorted(s) == sorted(t)
