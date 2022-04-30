# https://leetcode.com/problems/merge-two-sorted-lists/

#Definition for singly-linked list.
from typing import Optional


'''
Same Goal as what we did in Merge Sort Merge Process
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # creating a dummy node to handle edge case of inserting into a empty lists
    head = ptr = ListNode() # result

    while list1 and list2: # till either list is not consumed entirely
        if list2.val > list1.val:
            # take from list1
            ptr.next = list1  # attach ref of node to result
            list1 = list1.next # step 1 in list1
        else:
            # take from list2
            ptr.next = list2  # attach ref of node to result 
            list2 = list2.next # step 1 in list2

        ptr = ptr.next  # to add next element in result list

    if list1: # attach all rest elem of list1
        ptr.next = list1
    
    if list2: # attach all rest elem of list2
        ptr.next = list2 

    return head.next

if __name__ == '__main__':
    l3 = ListNode(4, None)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)

    j3 = ListNode(4, None)
    j2 = ListNode(3, j3)
    j1 = ListNode(1, j2)

    ans = mergeTwoLists(l1, j1)

    while ans:
        print(ans.val)
        ans = ans.next



        
    
            
        
        