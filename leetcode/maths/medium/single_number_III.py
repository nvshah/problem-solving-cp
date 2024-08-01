# https://leetcode.com/problems/single-number-iii/description/

from typing import List
from functools import reduce
from operator import xor

'''
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Use bitwise operation & basic math
group number into 2 category s.t. 
group 1 will hold one single number
group 2 will hold another single number & 
thus xor of each group will leave single numbers respectively

# Approach
<!-- Describe your approach to solving the problem. -->
1. find xor of all the given numbers
> xor(nums) = xor(two single number in nums)
2. find the lsb (ie first set bit from rhs) of above xor result
3. the lsb will be corresponding to a number whose first bit position (from lhs) will be the position where 2 single number's bit alters. & 
4. thus this position will act as pivot for dividing the numbers into 2 group

'''


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        all_xor = reduce(xor, nums) 
        # IDea: find first set bit position in xor (hence it would be definitely alternating/contrasting of 2 single number)
        # get lsb position binary format (by num & it's 2 complement = negative num)
        diff_bit = all_xor & -all_xor

        g1 = 0 # group 1
        g2 = 0 # group 2

        for n in nums:
            if n & diff_bit:
                g1 ^= n 
            else:
                g2 ^= n 
        
        return [g1, g2]




