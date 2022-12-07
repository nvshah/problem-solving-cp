# https://leetcode.com/problems/middle-of-the-linked-list/description/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = slow = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    return slow