# https://leetcode.com/problems/happy-number/

import operator as op
from functools import partial

def get_digits(n, func=None):
    '''
    return generator of digits
    if func provided then digit is mapped to that func & then returned
    '''
    while n != 0:
        n, r = divmod(n, 10)
        yield func(r) if func else r

def isHappy(n: int) -> bool:
    visited = set()
    while n not in visited:
        if n == 1:
            return True
        visited.add(n)
        n = sum(get_digits(n, lambda x: x**2))

    return False
