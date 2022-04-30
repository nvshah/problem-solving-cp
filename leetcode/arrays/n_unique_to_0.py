
# Que https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/


from typing import List
import itertools as it


def sumZero(n: int) -> List[int]:
    q, r = divmod(n, 2)
    return it.chain.from_iterable(((x, -x) for x in range(1, q+1))) \
        if not r \
        else it.chain((0,), it.chain.from_iterable(((x, -x) for x in range(1, n//2+1))))


n = 5
ans = sumZero(n)

print(*ans)
