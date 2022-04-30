# https://leetcode.com/problems/pascals-triangle/

from typing import List


def generate(numRows: int) -> List[List[int]]:
    prev = [1]
    ans = [prev]
    odd = False
    for i in range(2, numRows+1):
        u = i // 2
        f = [1] + [prev[j] + prev[j+1] for j in range(u-1)]
        if odd:
            prev = f + [prev[u-1]*2] + f[::-1]
        else:
            prev = f + f[::-1]
        odd = not odd
        ans.append(prev)
    return ans

def generate2(numRows: int) -> List[List[int]]:
    prev = [1]
    ans = [prev]
    for i in range(2, numRows+1):
        ready = [0, *prev, 0]
        prev = [ready[l] + ready[l+1] for l in range(i)]
        ans.append(prev)
    return ans

ans = generate2(7)
for r in ans:
    print(r)
