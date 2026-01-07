# https://leetcode.com/problems/majority-element/

from typing import List

"""
BOYER-MOORE ALGO
  
-> If in given array, 1 element appears more than n//2 times then this algo works

- Assume king's crown to be claimed by diff element
  & it will bethrown to one having maximum power (ie frequency/counts)

  Start with assuming the first element is king (ie with count 1)

  as we move froward many new element will claim for crown with their counts
   & this will affect current king's popularity (ie thereby decreasing power)

   When current king power reaches 0 ->
   next time if someone claim then crown-will be allocated to him 

- repeat till all element are processed

"""
from collections import Counter


def majorityElement3(nums: List[int]) -> int:
    """
    Boyer-Moore Voting Algo
    """
    res, count = 0, 0

    for n in nums:
        if count == 0:  # {n} will be next result
            res = n
        count += 1 if n == res else -1

    return res


def majorityElement1(nums: List[int]) -> int:
    """
    Using Hash-Map
    """
    return Counter(nums).most_common(1)[0][0]


def majorityElement2(nums: List[int]) -> int:
    """
    Boyer-Moore Voting Algo
    """
    king = nums[0]  # current claim to crown by first element
    power = 1  # freq count

    for n in nums[1:]:
        if power == 0:  # if current king has no power then this {n} can be next king
            king, power = n, 1
        else:
            if king == n:  # increase power of current king
                power += 1
            else:  # claim by someone else so weaken current king's power
                power -= 1

    return king


l = [3, 2, 3]
l = [2, 2, 1, 1, 1, 2, 2]
a = majorityElement2(l)
a2 = majorityElement1(l)
print(a, a2)
