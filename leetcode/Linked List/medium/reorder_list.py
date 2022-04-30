# https://leetcode.com/problems/reorder-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printSLL(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print()

def reorderList(head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #1 find the middle node using slow-fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # Slow pointer will now point to first half last element

        # reverse the links direction in second half
        second = slow.next 
        slow.next = None  # First half last element pointing to None (in case of Odd Nodes)
        prev = None
        while second:
            second.next, prev, second = prev, second, second.next

        # At the end or reversal seconnd will point to Null/None
        
        # Merge First & Second Half in alternating Way
        first, second = head, prev
        while second:  # as #second-half is = or < the first half
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, first.next
            first, second = temp1, temp2

head = [1,2,3,4]
n4 = ListNode(4, None)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
head = n1

printSLL(head)
reorderList(head)
printSLL(head)



