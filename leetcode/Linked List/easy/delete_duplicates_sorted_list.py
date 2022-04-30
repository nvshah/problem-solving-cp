# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        while p1:
            v1 = p1.val  # curr val
            p2 = p1.next # p2 -> check for next duplicate values to curr value {v1}
            while p2 and v1 == p2.val: # Skip duplicates value 
                p2 = p2.next
            p1.next = p2  # p2 -> now points to next unique value
            p1 = p2       # move ahead to check next duplicates
        return head