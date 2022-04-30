# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import Optional


'''
Logic ->

traverse till {left} node
keep track of immediate predecessor of {left} node i.e {leftPrev}
from left till right, make pointer's direction of each node, reverse
adjustment (left & right) nodes :-
-> make {left} node to point to {right}'s next node
-> make {leftPrev} to point to {right} node

Note :- using temp node to point to head inorder to handle case when {left} == 1
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    t = ListNode(0, head)  # temporary node pointing to head

    # reach at {left} position (i.e curr will point to {left})
    prev, curr = t, head 
    for _ in range(left-1):
        prev, curr = curr, curr.next
    
    leftPrev = prev  # pointer pointing to immediate left Most node of left
    # reverse logic :- just invert the pointing arrow direction
    for _ in range(right-left + 1):
        curr.next, prev, curr = prev, curr, curr.next 
    
    # handle the left and right node arrows/pointers
    leftPrev.next.next = curr # make point left node -> immediate next node of right node
    leftPrev.next = prev  # make point immediate predecessor of left -> to point to right node

    return t.next # original head
    






five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)
l = [one, two, three, four, five]

reverseBetween(l, 2, 4)

print([e.val for e in l])

        
            




