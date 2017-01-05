#7. Reverse Integer
'''Reverse digits of an integer.'''

def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    l = 0
    f = x if x>0 else -x
    while f:
        l,f = l*10 + f%10, int(f/10)
    if l < -(1 << 31) or l > (1 << 31) - 1:
        return 0
    return l if x>0 else -l