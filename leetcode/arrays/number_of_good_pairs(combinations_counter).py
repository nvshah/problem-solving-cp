from typing import List
import itertools as it
from collections import Counter as ctr

# Que -> https://leetcode.com/problems/number-of-good-pairs/


def numIdenticalPairs(nums: List[int]) -> int:
    return [
        (i, j) for i, j in it.combinations(
            range(len(nums)), 2) if (nums[i] == nums[j]) and (i < j)
    ]


def numIdenticalPairs_2(nums: List[int]) -> int:
    return sum([v*(v-1)//2 for v in ctr(nums).values() if v > 1])


print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(numIdenticalPairs_2([1, 2, 3, 1, 1, 3]))
