#400 Nth Digit

'''Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...'''

def findNthDigit(self, n):
    """
    :type n: int
    :rtype: int
    """
    start, size, step = 1, 1, 9
    while n > size * step:
        n, size, step, start = n - (size * step), size + 1, step * 10, start * 10
    return int(str(start + (n - 1) // size)[(n - 1) % size])