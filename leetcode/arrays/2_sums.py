# /usr/bin/python3

import itertools as it
from typing import List


class Solution:
    # Approach 1 Deprecated, (As this works only for Positive integers)
    def twoSum_a1(self, nums: List[int], target: int) -> List[int]:
        f_nums = (ne for ne in enumerate(nums) if ne[1] <= target)
        pairs = it.combinations(f_nums, 2)
        for ne1, ne2 in pairs:
            if ne1[1] + ne2[1] == target:
                return [ne1[0], ne2[0]]

    '''
    Idea -> seperate odds & even nums &
            odd = even + odd
            even = odd + odd | even + even
    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def isOdd(num):
            return bool(num % 2)

        odds = []
        evens = []

        for i in range(len(nums)):
            if isOdd(nums[i]):
                odds.append(i)
            else:
                evens.append(i)

        if isOdd(target):
            # Odd Number
            pairs = it.product(odds, evens)
        else:
            # Even Number
            pairs = it.chain(it.combinations(odds, 2),
                             it.combinations(evens, 2))

        for i1, i2 in pairs:
            if nums[i1] + nums[i2] == target:
                return [i1, i2]


'''
Much Better using Dict
'''


def twoSum(nums: List[int], target: int) -> List[int]:
    hash_map = dict()
    for i in range(len(nums)):
        if target - nums[i] in hash_map:
            return [hash_map[target-nums[i]], i]
        else:
            hash_map[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    ans = s.twoSum([2, 7, 11, 15], 9)
    print(ans)

    ans = s.twoSum([3, 2, 4], 6)
    print(ans)

    ans = s.twoSum([3, 3], 6)
    print(ans)

    ans = s.twoSum([-3, 4, 3, 9], 0)
    print(ans)
