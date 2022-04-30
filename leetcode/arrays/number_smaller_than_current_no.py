
from typing import List

# Que -> https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    l = len(nums)
    idx_sorted = sorted(range(l), key=lambda i: nums[i])  # Stable Sort
    result = [0] * l
    lv = 0
    for idx, ri in enumerate(idx_sorted[1:], start=1):
        if nums[ri] == nums[idx_sorted[idx-1]]:
            result[ri] = lv
        else:
            result[ri] = idx
        lv = result[ri]
    return result


def smallerNumbersThanCurrent3(nums: List[int]) -> List[int]:
    s_nums = sorted(nums)
    d = {}
    for i, n in enumerate(s_nums):
        if n not in d:
            d[n] = i
    return (d[n] for n in nums)


nums = [8, 1, 2, 2, 3]
ans = smallerNumbersThanCurrent(nums)
ans3 = smallerNumbersThanCurrent3(nums)

print(*ans3)
