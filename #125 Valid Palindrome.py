#125 Valid Palindrome

'''
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
'''

# ***re
import re
def isPalindrome(s):
    s = "".join(i for i in re.findall('[a-z0-9]',s.lower()))
    for i in range(int(len(s)/2)):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

