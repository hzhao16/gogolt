#389 Find the Difference
'''
Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then add one more letter at a random position.
Find the letter that was added in t.
'''

# ***Counter
from collections import Counter
def findTheDifference(s, t):
    return list(Counter(t)-Counter(s))[0]

# XOR
from operator import xor
def findTheDifference1(s, t):
    return chr(reduce(xor, map(ord, s + t)))