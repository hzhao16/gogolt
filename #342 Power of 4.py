#342 Power of 4
'''Given an integer (signed 32 bits), write a function to check whether it is a power of 4.'''

'''a^n - b^n = (a-b)(*****) '''

def ispower4(num):
	if num<=0:
        return False
    return (num&(num-1)==0 and (num-1)%3==0)

def my_ispower4(num):
    if num<=0:
        return False
    return (num&(num-1)==0 and (len(bin(num)))%2==1)