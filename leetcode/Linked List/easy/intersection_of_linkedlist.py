# https://leetcode.com/problems/intersection-of-two-linked-lists/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # For Intersection to Compare it would start comparing from min(l1, l2) elements

    # 1. Find length of first List
    lenA = 0
    travA = headA 
    while travA:
        lenA += 1
        travA = travA.next

    # 2. Find length of second List
    lenB = 0
    travB = headB
    while travB:
        lenB += 1
        travB = travB.next 
    
    # Skip first element from either Lists
    if lenA > lenB:
        toSkip = lenA - lenB 
        for _ in range(toSkip):
            headA = headA.next 
    elif lenB > lenA:
        toSkip = lenB - lenA 
        for _ in range(toSkip):
            headB = headB.next 
    
    # #elements to commpare for intersection
    cnt = min(lenA, lenB)
    for _ in range(cnt):
        if headA is headB:  # intersection point
            return headA 
        headA, headB = headA.next, headB.next
    return None

def getIntersectionNode2(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    '''
    Fast Pointer & Slow Pointer concept
    Concept :- at the end both has to travel {n + m} nodes to identify the inntersection point
    '''
    l1, l2 = headA, headB
    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
    return l1