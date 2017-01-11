#290. Word Pattern

'''
Given a pattern and a string str, 
find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
'''

#*** zip ***
def wordPattern(p, str1):
    if len(p)!=len(str1.split(" ")):
            return False
    return len(set([i for i in zip(p, str1.split(" "))]))==len(set(p))==len(set(str1.split(" ")))

