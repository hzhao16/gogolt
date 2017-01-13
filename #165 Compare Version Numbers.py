#165 Compare Version Numbers

'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", 
it is the fifth second-level revision of the second first-level revision.
'''

def compareVersion(version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    n = max(len(v1),len(v2))
    for i in range(n):
        v11 = int(v1[i]) if i<len(v1) else 0
        v22 = int(v2[i]) if i<len(v2) else 0
        if v11<v22:
            return -1
        elif v11>v22:
            return 1
    return 0