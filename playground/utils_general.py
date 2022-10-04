import itertools as it
from operator import eq

def isPalindrome(s):
    return all(it.starmap(eq, zip(s, reversed(s))))

n = 'sdss'
print(isPalindrome(n))