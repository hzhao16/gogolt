#14. Longest Common Prefix

'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

# ***
def longestCommonPrefix(strs):
    l = ""
    for i in range(len(strs[0])):
        for j in range(1,len(strs)):
            try:
                if strs[j][i]!=strs[0][i]:
                    return l
            except:
                return l
        l+=strs[0][i]
    return l
strs=['babe','babc','babbb']
longestCommonPrefix(strs)