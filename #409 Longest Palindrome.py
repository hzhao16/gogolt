#409 Longest Palindrome
'''
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built with those letters.
'''

def longestPalindrome(s):
	d = {}
    c = 0
    x = 0
    for i in s:
        d[i]=d.get(i,0)+1
    for v in d.values():
        if v%2:
            c+=v-1
            x = 1
        else:
            c+=v
    return c+x