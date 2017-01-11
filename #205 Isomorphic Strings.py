#205 Isomorphic Strings
'''
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

'''

# *** dict
def isIsomorphic(s, t):
    d1,d2={},{}
    n = len(s)
    for i in range(n):
        
        if d1.get(s[i],0)==0:
            d1[s[i]]=[]
        d1[s[i]].append(i)
        # d1[s[i]] = d1.get(s[i],[])+[i]
        if d2.get(t[i],0)==0:
            d2[t[i]]=[]
        d2[t[i]].append(i)
    return sorted(d1.values())==sorted(d2.values())
# zip + set
def isIsomorphic1(s, t):
    return len(set(zip(s,t)))==len(set(s))==len(set(t))

# .find
def isIsomorphic2(s, t): 
    return [s.find(i) for i in s] == [t.find(j) for j in t]   
def isIsomorphic3(s, t):
    return map(s.find, s) == map(t.find, t)