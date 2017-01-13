#345 Reverse Vowels of a String
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''

# *** 2 pointers

def reverseVowels(s):
    v = set('aeiouAEIOU')
    i = 0
    j = len(s)-1
    s = list(s)
    while i<j:
        if s[i] in v and s[j] in v:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        else:
            if s[i] not in v:
                i+=1
            if s[j] not in v:
                j-=1
    return "".join(i for i in s)