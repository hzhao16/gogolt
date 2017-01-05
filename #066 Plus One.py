#66 Plus One

'''Given a non-negative number represented as an array of digits, plus one to the number.'''

def plusOne(digit):
    n = len(digit)
    i=n-1
    while i>=0:
        if digit[i]<9:
            digit[i]+=1
            return digit
        else:
            digit[i]=0
        i -=1
    # for case when '9999'    
    new = [0]*(n+1)
    new[0]=1
    return new
