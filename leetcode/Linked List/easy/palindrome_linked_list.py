# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome1(head: Optional[ListNode]) -> bool:
    '''Time Efficient'''
    arr = []
    while head:
        arr.append(head.val)
        head = head.next 
    
    l, r = 0, len(head)-1
    while l < r:
        if arr[l] != arr[r]:
            return False 
    
    return True 

def isPalindrome2(head: Optional[ListNode]) -> bool:
    '''Space Efficient (Fast & Slow Pointers)'''
    fast, slow = head, head 
    
    # Find Middle (ie Slow Pointer points to)
    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next 
    
    # Reverse Second Half
    prev = None 
    while slow:
        slow.next, slow, prev = prev, slow.next, slow 
    
    # Compare
    left, right = head, prev 
    while right: # Until right pointers reaches the midpoint
        if left.val != right.val:
            return False 
        left, right = left.next, right.next 

    return True 
