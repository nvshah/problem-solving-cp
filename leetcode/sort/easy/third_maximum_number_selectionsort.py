# https://leetcode.com/problems/third-maximum-number/

from typing import List

def thirdMax(nums: List[int]) -> int:
    l = set(nums)
    if len(l) <= 2:
        return max(l)
    else:
        return sorted(set(nums), reverse=True)[2]

def thirdMax2(nums: List[int]) -> int:
    '''Using Selection Sort'''
    s = set(nums)  # set inorder to discard repeatable max element consideration
    if len(s) <= 2:  # Edge Case as per problem
        return max(s)
    for _ in range(2):  # remove first 2 maximum from set
        s.remove(max(s))
    return max(s)  # third max will be max from current set