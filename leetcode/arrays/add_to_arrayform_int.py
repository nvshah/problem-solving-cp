# https: // leetcode.com/problems/add-to-array-form-of-integer/


from typing import List
from math import log10


def addToArrayForm(num: List[int], k: int) -> List[int]:
    return map(int, str(int(''.join(map(str, num))) + k))


def addToArrayForm2(num: List[int], k: int) -> List[int]:
    n1_l = len(num)
    n2_l = log10(k) + 1
    new_res = [0] * max(n1_l, n2_l)

    carry = 0

    if n1_l > n2_l:
        for i in range(n1_l-1, -1, -1):
            m = k % 10
            carry, r = divmod(carry + m + num[i], 10)
            new_res[i] = r
    else:
        while k != 0:
            m = k % 10
            carry, r = divmod(carry + m + num[i], 10)
            new_res[i] = r

    while(k != 0):
        trav = 0
        k, m = divmod(k, 10)
        carry, remainder = divmod(carry + m + num, 10)
        new_res[trav] = remainder
        trav -= 1


num = [1, 2, 0, 0]
k = 34

ans = addToArrayForm(num, k)

print(*ans)
