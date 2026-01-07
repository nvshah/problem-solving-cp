# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/


from typing import List

"""
1 2 3 4 

4 1 2 3 
3 4 1 2
2 3 4 1 

Hence in a rotation there can be max k permutations where k is len 
-
We can mirror same array and can get all combinations, why ?
because it will ensure we will have k elements (next) for each element in original array

So getting combination is deal via mirror 
Now to identify sorting order 
we will use sliding window 
"""


class Solution:
    def check(self, nums: List[int]) -> bool:
        size = len(nums)
        clone_size = size * 2

        l, r = 0, 1

        if size == 1:  # edge case
            return True

        while l < size and r < clone_size:
            j = r % size
            i = (r - 1) % size

            if nums[i] > nums[j]:
                l = r  # reset
            elif r - l + 1 == size:
                return True  # found window i.e non-decreasing

            r += 1

        return False


s = Solution()
s.check([3, 4, 5, 1, 2])
