#204 Count Primes

'''Count the number of prime numbers less than a non-negative number, n.'''

'''Sieve of Eratosthenes'''

def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        isprime = [1]*n
        i=2
        while i*i<n:
            if isprime[i]:
                for j in range(i*i,n,i):
                    isprime[j]=0
            i+=1
        return sum(isprime[2:])