# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:   
    dummy = ListNode(-1, next=head)
    left = dummy   # slow 
    right = head   # fast

    # maintain (n+1) gap between right & left
    while n > 0:
        right, n = right.next, n-1 
    
    # Traverese entire list with [right]
    while right:
        left, right = left.next, right.next

    # Now left is at the node whose next node is the one to be deleted
    # i.e left is pointing to n+1th node from end as of now

    # delete nth node from end
    left.next = left.next.next

    return dummy.next