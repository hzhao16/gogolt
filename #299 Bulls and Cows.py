#299 Bulls and Cows

'''
You are playing the following Bulls and Cows game with your friend: 
You write down a number and ask your friend to guess what the number is. 
Each time your friend makes a guess, you provide a hint that indicates 
how many digits in said guess match your secret number exactly in both digit and position (called "bulls") 
and how many digits match the secret number but locate in the wrong position (called "cows"). 
Your friend will use successive guesses and hints to eventually derive the secret number.

Secret number:  "1807"
Friend's guess: "7810"

Write a function to return a hint according to the secret number and friend's guess, 
use A to indicate the bulls and B to indicate the cows. 
In the above example, your function should return "1A3B".
'''

def getHint(self, secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    from collections import Counter
    n = len(secret)
    a = 0
    for i in range(n):
        if secret[i] == guess[i]:
            a+=1
    # a = len([i for i in range(n) if secret[i]==guess[i]])
    total = sum((Counter(secret)&Counter(guess)).values())
    b = total-a
    return '%dA%dB'%(a,b)