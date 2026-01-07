# https://leetcode.com/problems/subsets/

from itertools import compress
from typing import List


def subsets3(nums: list[int]) -> List[List[int]]:
    """
    Use Iteration & Bit Manipulation
    """
    n = len(nums)
    subsets = 2**n
    res = []
    for i in range(subsets):  # 0...2^n <- current mask no = {i}
        binary = format(i, f"0{n}b")  # format i in binary
        mask = [int(b) for b in binary]  # bit mask
        sel = list(compress(nums, mask))  # select nums as per bit-mask
        res.append(sel)
    return res


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Use Recursion to obtain sublists
    When you encounter the Leaf Node in DT, you will get one of possible sublist
    """

    res = []
    subset = []  # temp list store the current sublist members
    size = len(nums)

    def dfs(i):
        """
        i -> pos at where from we need to look for subsets
        """
        if i == size:  # Reach to the Leaf of DT where you get one of possible subset
            res.append(subset.copy())
            return

        # Take num[i]
        subset.append(nums[i])
        dfs(i + 1)

        # Check for subsets possibilities discarding the nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


def subsets2(nums: List[int]) -> List[List[int]]:
    """
    Use Recursion to obtain sublists
    When you encounter the Leaf Node in DT, you will get one of possible sublist
    """

    def dfs(p, up):
        """
        p -> processed
        up -> unprocessed
        """
        if not up:  # Reach to the Leaf of DT where you get one of possible subset
            return [p]

        f = up[0]  # first
        remains = up[1:]  # to be processed in future
        l = dfs([*p, f], remains)  # include first
        r = dfs(p, remains)  # exclude first

        return [*l, *r]

    return dfs([], nums)


def subsets4(nums: List[int]) -> List[List[int]]:
    """
    Use Iteration & Bit Manipulation
    """
    n = len(nums)
    subsets = 1 << n  # 2^n
    res = []
    for i in range(subsets):  # 0...2^n <- current mask no = {i}
        sel = []
        # check each position/bit if set or not in mask represented by i
        for j in range(n):
            if i & (1 << j):
                # jth bit is set !! so select the number at jth position
                sel.append(nums[j])
        res.append(sel)
    return res
