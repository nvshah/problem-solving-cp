# https://leetcode.com/problems/contains-duplicate/

from typing import List
from collections import defaultdict

def containsDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

def containsDuplicate1(nums: List[int]) -> bool:
    s = set()
    for n in nums:
        if n in s:
            return True 
        s.add(n)
    return False

def containsDuplicate2(nums: List[int]) -> bool:
    d = defaultdict(int)
    for n in nums:
        if d[n]:
            return True 
        d[n] += 1
    return False