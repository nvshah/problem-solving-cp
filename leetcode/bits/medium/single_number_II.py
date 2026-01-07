# https://leetcode.com/problems/single-number-ii/description/

# Soln Ref :- https://algo.monster/liteproblems/137

from typing import List
from collections import Counter

"""
Soln 4 

The key understanding in solving this problem is recognizing that if we add up the same bits of all numbers in nums, 
since all but one number appears three times, 
the sum of bits in any position must be a multiple of three if the unique number does not contribute a bit in that position.

The idea is to count the number of times each bit is set (1) in all the numbers. 
If a bit is set three times, then it is irrelevant since every number except one appears three times. 
Only the bits that are set once or twice will contribute to the single number.

Here's a step-by-step approach:

    1. Initialize two variables (ones and twos) that will represent bits that have appeared once or twice respectively.
    2. Traverse through the array, updating ones and twos using bit manipulation.
    3. The key idea is to clear the bits from ones and twos if a number appears three times.
"""


def singleNumber_1(nums: List[int]) -> int:
    """HashMap
    T.C := O(n) * O(logn)  // logn for creating hashmap (avg case)
    S.C := O(n)
    """
    freqs = Counter(nums)
    for num, freq in freqs.items():
        if freq == 1:
            return num


def singleNumber_2(nums: List[int]) -> int:
    """bitwise solution
    Idea :-
    except 1 all the numbers are repeated thrice
    hence their set bits also will be repeated thrice (ie multiple of 3)
    => So the bits (positions) which do not have total count in multiple of 3 insinuate that this bit is set in a number which is single

    T.C := O(32 * n)
    S.C := O(1)
    """
    single = 0
    for pos in range(32):  # pos := position of bit-index into consideration
        bit_mask = 1 << pos
        # calculate set-bit (ie 1) count for bit-index `pos`
        set_bit_count = 0
        for n in nums:
            is_set = n & bit_mask
            if is_set:
                set_bit_count += 1

        if set_bit_count % 3 == 1:
            # not multiple of 3 hence this bit (at `pos`) is set in single number
            single |= bit_mask  # set the bit at `pos` in anticipated single number
    return single


def singleNumber_3(nums: List[int]) -> int:
    """Sort | Logic
    Idea :-
    Pattern

    T.C := O(n log n)
    S.C := O(1)
    """
    nums.sort()

    for i in range(1, len(nums), 3):
        if nums[i - 1] != nums[i]:
            return nums[i - 1]

    return nums[-1]  # single number present at last


def singleNumber_4(nums: List[int]) -> int:
    """Digital Logic | State machine

    Idea :-  Mod 3 Counting (State Machine)

    Key Operations:
    1. Set a bit in ones if it has appeared exactly once (ie 1 % 3) so far.
    2. Set a bit in twos if it has appeared exactly twice (ie 2 % 3) so far.
    3. Clear the bits (set to 0) from both ones and twos if the bit has appeared three times.

    How ?
    -
    ones = (ones ^ n) & ~twos
    twos = (twos ^ n) & ~ones

    (consider count in mod3 state)
    ones -> track the bits that's count is 1 till now (by setting them in 32 bit repr)
    twos -> track the bits that's count is 2 till now (by setting them in 32 bit repr)

    T.C := O(n)
    S.C := O(1)
    """
    # `ones` track bit-indexes whose total-bit-count = (1 % 3) = 1 , at a moment
    ones = 0
    # `twos` track bit-indexes whose total-bit-count = (2 % 3) = 2 , at a moment
    twos = 0

    for num in nums:
        # (ones ^ num)
        #  - set (ie 1) bit positions in ones, as of num // for first & third appearance
        #  - unset bit (ie 0) positions in ones, as of num  // for second appearance
        # (~twos) will help unsetting bit in ones // for third appearance
        ones = (ones ^ num) & ~twos
        # (twos ^ num)
        #  - unset (ie 0) bit positions in ones, as of num // for first & third appearance
        #  - set (ie 1) bit positions in ones, as of num // for second appearance
        # (~ones) will help unsetting bit in twos  // for first appearance
        twos = (twos ^ num) & ~ones

    return ones


nums = [2, 2, 3, 2]
ans = singleNumber_2(nums)
print(ans)
