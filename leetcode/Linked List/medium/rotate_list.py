# https://leetcode.com/problems/rotate-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head: return head # Edge Case

    # 1. find length & last node (ie tail)
    length, tail = 1, head 
    while tail.next:
        length, tail = length+1, tail.next
    
    # 2. Find actual rotation (in effect)
    r = k % length
    if r == 0:
        return head  # no rotation effectively 

    # 3. Go to Pivot (ie effectively last node after performing rotations {r})
    curr = head 
    for i in range(length-r-1):
        curr = curr.next 
    
    # 4. Adjustment 
    #    NOTE :- {curr} -> is pivot ie pointing eventually to effective tail node of new List after rotation
    newHead = curr.next 
    curr.next = None   # make {curr} as newTail
    tail.next = head   # rotate = brinng last k elem in front

    return newHead 


        