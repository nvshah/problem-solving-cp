# https://leetcode.com/problems/remove-linked-list-elements/https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(-1, head)
    p1, p2 = dummy, head  # 2 pointers

    while p2:
        nxt = p2.next 
        if p2.val == val:
            p1.next = nxt  # remove {p2}
        else:
            p1 = p1.next  # move {p1} by 1 step
        p2 = nxt  # move {p2} by 1 step
    return dummy.next 
        