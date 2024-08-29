# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
from typing import List
import bisect


# APPROACH 1 (Manual Binary Search IMPL)
def successfulPairs_1(spells: List[int], potions: List[int], success: int) -> List[int]:
    '''T.C :- O((n+m)*logm)'''
    # 1. sort the [potions]
    potions.sort()

    size = len(potions)
    res = []
    # 2. Binary Search for each spell, to find left-most potion
    for spell in spells:
        # Find smallest possible potion position
        l, r = 0, size - 1
        # at the end, [l] will point to pos for smallest eligible potion
        while l <= r:
            m = (l + r) // 2
            if potions[m] * spell >= success:
                # eligible potion
                r = m - 1
            else:
                # ineligible potion // hence search for more large potion
                l = m + 1

        # ? now [l] is index position hence denotes #elems besides it in [potions]
        total_eligibles = size - l
        res.append(total_eligibles)

    return res


# APPROACH 2 (Using Bisect)
def successfulPairs_1(spells: List[int], potions: List[int], success: int) -> List[int]:
    '''T.C :- O((n+m)*logm)'''
    potions.sort()
    total = len(potions)
    return [
        total
        - bisect.bisect_left(
            potions,
            success,
            key= lambda potion: potion*spell
        )
        for spell in spells
    ]
