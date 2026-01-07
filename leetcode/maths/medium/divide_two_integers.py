# https://leetcode.com/problems/divide-two-integers/submissions/

from math import copysign, log2


def divide(dividend: int, divisor: int) -> int:
    """T.C := O(log(dividend)) // base2

    Exponentially remove larger multipler of divisor from dividend in each outer while loop iteration
    """
    q = 0  # quotient
    a, b = abs(dividend), abs(divisor)  # a/b
    cnt = 1
    while a >= b:
        # Exponential reach out
        tmp = b
        mult = 1  # multiplier to tmp (ie mult * tmp = cur divisor)
        while a >= tmp:
            a -= tmp  # division & remainder
            q += mult  # current quotient
            mult += mult  # exponential increase in divisor val
            tmp += tmp  #

        print(cnt, ":", log2(mult), q, b)
        cnt += 1

    if (dividend >= 0 and divisor < 0) or (divisor > 0 and dividend <= 0):
        q = -q

    m = 2**31

    ans = max(-m, min(m - 1, q))

    return ans


def divide(dividend, divisor):
    """Reverse Engineering"""
    if dividend == divisor:
        return 1
    if divisor == 1:
        return dividend

    # -ve when only one of `num` or `divisor` is -ve
    sign = int(copysign(1, dividend * divisor))

    n = abs(dividend)
    d = abs(divisor)

    ans = 0

    while n >= d:
        # try to remove next bigger part (of answer) from n !
        b = 0  # identify bit position of multiplier
        # while n >= (d * (2**(b+1))):
        while n >= (d << b + 1):  # d << b+1 := d * pow(2, b+1)
            b += 1

        # multiplier = (2**b)
        multiplier = 1 << b  # := 2**b

        n -= d * multiplier
        ans += multiplier

    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    if ans > INT_MAX:  # ans is always positive
        if sign > 0:
            return INT_MAX
        else:
            return INT_MIN

    return ans * sign


a = divide(113, 2)
print(a)
