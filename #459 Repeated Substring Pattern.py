#459. Repeated Substring Pattern

'''
Given a non-empty string check if it can be constructed by taking a substring of it 
and appending multiple copies of the substring together.

'''


def repeatedSubstringPattern(strstr):
    if not strstr:
        return False
    # the first and last element of s is the start and end of the pattern
    s = (strstr+strstr)[1:-1]
    # if strstr is not in s, i.e., i=-1, then not a repeated string.
    i = s.find(strstr)
    # the repeated substring pattern will have length i+1
    print(strstr[0:i+1])
    return i!=-1

strstr = 'abab'
repeatedSubstringPattern(strstr)