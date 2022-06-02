# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
from typing import Optional
from unittest import skip

'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning 
and the kth node from the end (the list is 1-indexed).

Eg
 IP :- head = [1,2,3,4,5], k = 2
 OP :- [1,4,3,2,5]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Better Approach
def swapNodes2(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    '''Single Traversal'''
    curr = head
    l = k-1
    while l:
        curr, l = curr.next, l-1
    
    p1 = curr
    p2 = head
    while curr.next:
        curr, p2 = curr.next, p2.next

    p1.val, p2.val = p2.val, p1.val
    return head

def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # 1. Find the length of the linked list
    curr, n = head, 0  # n := #nodes in linkedlist
    while curr:
        curr, n = curr.next, n+1
    
    # skip1 := #nodes before kth node from start (ie Skip from start for left node)
    # skip2 := #nodes before kth node from the end (ie Skip from Start for right node)
    skip1, skip2 = k-1, n-k
    if skip1 == skip2:
        return head # no swap is required

    if skip1 > skip2:
        skip1, skip2 = skip2, skip1 

    p2 = head # ptr 2

    i = 0
    # Jump to first node in Swapped pair
    #for i in range(skip1):
    while i != skip1:
        p2, i = p2.next, i+1 
    
    # 1 of node in pair
    p1 = p2  # ptr 1 

    i += 1

    # Jump to first node in Swapped pair
    #for j in range(i+1, r-l+1):
    while i != skip2:
        p2, i = p2.next, i+1
    
    p1.val, p2.val = p2.val, p1.val

    return head






            

        


        