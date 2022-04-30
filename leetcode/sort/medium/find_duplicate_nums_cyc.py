# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List
from collections import defaultdict


def findDuplicate(nums: List[int]) -> int:
    i = 0
    while i < len(nums):
        c_i = nums[i]-1
        if c_i != i:  # element is at wrong index
            if nums[c_i] == nums[i]:
                return nums[i]  #duplicate found
            nums[i], nums[c_i] = nums[c_i], nums[i]
        else:
            i += 1


def findDuplicate_ctr(nums):
    d = defaultdict(int)
    for n in nums:
        if d[n] == 1:
            return n 
        d[n] += 1

def findDuplicate_floyd(nums: List[int]) -> int:
    # Floyd Algo 

    # Step 1. Find the Meeting Point of fast & slow pointer
    fast, slow = 0, 0  # both pointing to idxes 
    while True:
        slow = nums[slow]        # 1 step
        fast = nums[nums[fast]]  # 2 steps

        if fast == slow:  # reach meeting point in cycle
            break 
    
    # Step 2. Find the Cycle Starting Point 
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2 : # start point of cycle 
            return slow    # answer will be index & not val


nums = [1,3,4,2,2]  # 2
nums = [3,1,3,4,2]  # 3
nums = [1,1] # 1
nums = [1,1,2] # 1
print(findDuplicate(nums))