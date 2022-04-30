# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional

'''
Idea :- Floyd's Algo
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head 
    # Do-While 
    while fast and fast.next:  # till fast doesn't exhaust Linked List
        slow, fast = slow.next, fast.next.next 
        if slow == fast:  # slow & fast met thus cycle exists
            return True  
    return False