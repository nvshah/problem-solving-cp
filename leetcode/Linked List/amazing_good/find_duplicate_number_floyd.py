# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List

'''
Idea :- Floyd Algo Detection for Simulated Linked List

 Note :- There will be elem in range 1 -> n 
         & 1 duplicate

         So we can consider this array structure as Linked List where 
         each val is pointing to next index in LinnkedList 

         & any 1 index will be pointed by 2 element of array (ie duplicate)

         Also the first idx ie {0} will not be pointed by any of the vals 
         So we can consider initial point as first idx {0} as starting point of traversal 

        Thus we have simulated the Linked List from array till now
        &
        Cycle is going to exists for sure !!

        Now :- We will apply Floyd Algo to detect the starting point for Cycle Point

NOTE :- answer will be that index of array which get multiple links         

'''

def findDuplicate(nums: List[int]) -> int:
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
