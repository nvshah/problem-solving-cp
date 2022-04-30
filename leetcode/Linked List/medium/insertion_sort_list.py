# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        trav = head
        while trav.next:
            nxt = trav.next  # next node to {trav}
            if nxt.val < trav.val:
                trav.next = nxt.next  # remove {nxt} from its place
                
                # Find pos for nextVal in already Sorted Array
                prev, curr = dummy, head
                while nxt.val >= curr.val:
                    curr, prev = curr.next, curr
                
                # Shift the {nxt} to its appropriate pos ie between {prev} & {curr}
                prev.next = nxt
                nxt.next = curr
            else:    
                trav = trav.next # traverse ahead
            
        return dummy.next
                    
                
            