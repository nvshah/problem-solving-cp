# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/


from typing import List
from functools import reduce


def longestSubarray(nums: List[int]) -> int:
    """
    Idea :
    whenever we do bitwise and of 2 num let say a & b
    then result will hold value lesser than a if a > b
    if b > a, then result will hold value lesser than b

    Hence we need to find consecutive subarry s.t all elements are equal & that element is max among all elements in arr

    This problem is complicated way of asking to find longest subarray with max elements
    """
    # 1. If n < cur_max, n & cur_max < cur_max
    # 2. If n > cur_max, n & cur_max < n
    # 3. If n == cur_max, n & cur_max = n
    cur_size = 0
    cur_max = 0
    res = (0, 0)  # (elem, count)
    for n in nums:
        if n > cur_max:
            cur_max = n
            cur_size = 1
            res = 0  # reset as found new larger number
        elif n == cur_max:
            cur_size += 1
        else:
            cur_size = 0
        res = max(res, cur_size)
    return res


def longestSubarray2(nums: List[int]) -> int:
    """
    Idea :
    whenever we do bitwise and of 2 num let say a & b
    then result will hold value lesser than a if a > b
    if b > a, then result will hold value lesser than b

    Hence we need to find consecutive subarry s.t all elements are equal & that element is max among all elements in arr

    This problem is complicated way of asking to find longest subarray with max elements
    """
    # 1. If n < cur_max, n & cur_max < cur_max
    # 2. If n > cur_max, n & cur_max < n
    # 3. If n == cur_max, n & cur_max = n
    cur_size = 0
    cur_max = 0
    res = (0, 0)  # (elem, count)
    for n in nums:
        if n == cur_max:
            cur_size += 1
        else:
            cur_size = 1 if n > cur_max else 0
            cur_max = max(cur_max, n)
        res = max(res, (cur_max, cur_size))
    return res[1]


def longestSubarray2(nums: List[int]) -> int:
    """
    Idea :
    Find length of longest subbarray having consecutive max element
    """
    target = max(nums)
    cur_max = 0
    res = 0
    for n in nums:
        if n == target:
            cur_max += 1
        else:
            cur_max = 0
        res = max(cur_max, res)
    return res


nums = [96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 279979]
nums = [1, 2, 3, 3, 4, 3, 3, 3, 5, 5, 3, 3]

ans = longestSubarray(nums)
print(ans)
