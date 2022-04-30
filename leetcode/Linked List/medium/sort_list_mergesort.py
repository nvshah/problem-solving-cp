# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getMid(self, head: ListNode):
        '''
        Get the middle node via using slow/fast pointer
        '''
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next       # step by 1
            fast = fast.next.next  # step by 2

        return slow  # at the end slow will be pointing to middle node of linked list

    def merge(self, ll1: ListNode, ll2: ListNode):
        '''
        :param ll1 :- linked list 1
        :param ll2 :- linked list 2
        Merge the 2 linked lists, both being sorted already into single sorted linked list
        T.C = O(n)
        '''
        tail = head = ListNode() # in case to handle empty node in either of list

        while ll1 and ll2:
            if ll1.val > ll2.val:
                tail.next = ll2  # append smaller {ll2} to tail of final linked list
                ll2 = ll2.next 
            else:
                tail.next = ll1  # append smaller {ll1} to tail of final linked list
                ll1 = ll1.next 
            tail = tail.next  # update {tail} as 1 element gets being added in current loop
        
        # if elements left in {ll1} add all to end ie {tail}
        if ll1:
            tail.next = ll1
        # if elements left in {ll2} add all to end ie {tail}
        if ll2:
            tail.next = ll2 
        
        return head.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        As we have linkedList so it can be done easily in O(1) Space Complexity
        T.C = O(n*logn)
        S.C = O(1)
        (Inplace sorting)
        '''
        if not head or not head.next: # 0 or 1 node only in linkedlist
            return head 
        
        # 1. split the Linked List into 2 half
        mid = self.getMid(head) # mid will be the last node of left part
        left = head
        right = mid.next  # as the right half will start immediate next to mid
        mid.next = None  # seperate out the first half

        # 2. sort the halves
        l = self.sortList(left)  # head of left part after sorted
        r = self.sortList(right) # head of right part after sorted

        # 3. merge the halves
        return self.merge(l, r)