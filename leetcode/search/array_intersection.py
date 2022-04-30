# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)