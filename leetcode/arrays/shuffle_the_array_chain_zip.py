from typing import List
import itertools as it

# Que -> https://leetcode.com/problems/shuffle-the-array/


def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res


def shuffle_2(nums, n):
    # Faster
    return it.chain.from_iterable(zip(nums[:n], nums[n:]))


a1 = shuffle([2, 5, 1, 3, 4, 7], 3)
a2 = shuffle_2([2, 5, 1, 3, 4, 7], 3)

print(a1)
print(*a2)
