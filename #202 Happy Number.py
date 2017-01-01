#202 Happy Number
'''A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits,
 and repeat the process until the number equals 1 (where it will stay), 
 or it loops endlessly in a cycle which does not include 1. 
 Those numbers for which this process ends in 1 are happy numbers.'''


def sq(n):
    return sum([int(i)**2 for i in str(n)])

 '''1. check if sqr(num) in list'''
 def isHappy1(num):
    thelist = []
    #thelist = set()
    while num!=1 and num not in thelist:
        thelist.append(num)
        #thelist.add(num)
        num = sq(num)
    return num==1

'''2. 2 pointers'''
def isHappy2(n):
    slow= n
    fast = sq(n)
    while slow!=fast:
        slow = sq(slow)
        fast = sq(sq(fast))
    return fast==1


