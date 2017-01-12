#344 Reverse String

'''Write a function that takes a string as input and returns the string reversed.'''

# ***swap
def reverseString(s):
    n = len(s)
    s = list(s)
    for i in range(int(n/2)):
        s[i],s[n-i-1] = s[n-i-1],s[i]
    return "".join(i for i in s)

# slicing
def reverseString(s):
	return s[::-1]