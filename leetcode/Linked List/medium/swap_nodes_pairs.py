# https://leetcode.com/problems/swap-nodes-in-pairs/

'''
Que
Given a linked list, swap every two adjacent nodes and 
return its head. You must solve the problem without modifying 
the values in the list's nodes (i.e., only nodes themselves may be changed.)


'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1, head)  # dummy node at start
    prev, curr = dummy, head    # prev points to pair & curr is first node in pair

    while curr and curr.next:
        # save ptrs for next pair
        second = curr.next
        nextPair = second.next 
         

        # Swap the nodes 
        second.next = curr    # relocate second node to first pos
        curr.next = nextPair  # connect curr pair to next pair
        prev.next = second   # link prev node to swapped Pair

        # Update pointers
        prev, curr = curr, nextPair

    return dummy.next


        