# https://leetcode.com/problems/partition-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    leftHead, rightHead = ListNode(), ListNode()
    leftTail, rightTail = leftHead, rightHead

    while head:
        if head.val < x:
            leftTail.next = head 
            leftTail = leftTail.next 
        else:
            rightTail.next = head 
            rightTail = rightTail.next 
        head = head.next 
    
    leftTail.next = rightHead.next 
    rightTail.next = None 

    return leftHead.next
