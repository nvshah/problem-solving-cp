# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Find mid node using 2 pointer technique
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow, prev = prev, slow.next, slow
            
        # Now {slow} is pointing to first element of second half & 
        # {prev} is pointing to last element of first half
        # Thus we will traverse inside-out from middle to check each twin pair
        
        # 2. Traverse inside-out, checking each twin pair
        res = 0
        while slow:
            pair = prev.val + slow.val
            res = max(res, pair)
            slow, prev = slow.next, prev.next
        return res
        