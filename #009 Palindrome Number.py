#9. Palindrome Number

'''Determine whether an integer is a palindrome. Do this without extra space.'''

'''Same with #7'''
def palindrome(num):
    if num<0:
        return False
    a = 0
    b = num
    while b:
        a,b = a*10 + b%10, int(b/10)
    if a < -(1<<31) or a > (1<<31)-1:
        return False 
    if a==num:
        return a
    else:
        return False

'''Handlig Overflow -> stop loop before reversing the last digit'''
def palindrome_1(num):
    if num<0:
        return False
    a = 0
    b = num
    while b>=10:
        a,b = a*10 + b%10, int(b/10)
    return a == int(num/10) and b == num%10
