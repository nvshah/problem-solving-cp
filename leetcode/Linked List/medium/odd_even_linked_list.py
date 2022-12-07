# https://leetcode.com/problems/odd-even-linked-list/description/
from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head: return head 
    evenHead = head.next  # O(1)
    if not evenHead: return head

    first, second = head, head.next        
    while second and second.next:  # till next odd node exists
        third, fourth = second.next, second.next.next
        first.next, second.next = third, fourth
        first, second = third, fourth

    # Now first is referring the last odd node
    first.next = evenHead  # connect last odd node to first even node 
    return head