# https://leetcode.com/problems/guess-number-higher-or-lower/

# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

import random


def guess(num: int) -> int:
    return 0 if picked == num else 1 if picked > num else -1

def guessNumber(n: int) -> int:
    s, e = 1, n
    while True:
        m = (s + e) // 2
        g = guess(m)
        if g == 0:
            return m
        elif g == 1:
            s = m + 1
        else: 
            e = m - 1

if __name__ == '__main__':
    n = 20
    picked = random.randrange(1, 20)

    print('Picked-> ', picked)
    ans = guessNumber(n)

    print('Founded-> ', ans)


    