# https://leetcode.com/problems/merge-k-sorted-lists/

import itertools as it

from typing import List, Optional
from math import ceil, log2

# --- Utils

def segregate_to_groups(lst, grpSize=2, fillVal = None):
    ''' Eg -> 
          lst = [1,2,3,4,5] 
          size = 2 
          => ans := [(1,2), (3,4), (5, None)] 
    '''
    lst_iter = iter(lst)
    return it.zip_longest(*it.repeat(lst_iter, grpSize), fillvalue=fillVal)

def merge_two_lists(l1, l2):
    # creating a dummy node to handle edge case of inserting into a empty lists
    head = ptr = ListNode() # result
    while l1 and l2: # till either list is not consumed entirely
        if l2.val > l1.val:
            ptr.next = l1  # take from l1
            l1 = l1.next # move ahead in l1
        else:
            ptr.next = l2  # take from l2
            l2 = l2.next # move ahead in l2
        ptr = ptr.next 
    if l1: # attach all rest elem of l1
        ptr.next = l1
    elif l2: # attach all rest elem of l2
        ptr.next = l2 
    return head.next

# ---
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    ''' Use merge sort logic to perform merge of k sorted Linked List in n*O(logK) time 
        Explaination :-
          O(n) for each merge
          O(logK) merges :- O(logK) * n // T.C 
    '''
    if not len(lists): return None
    mergedLists = lists
    # Do till all lists are not merge into sinngle lists
    while len(mergedLists) != 1:
        # merge each sequential parit of group of {mergedLists}
        *mergedLists, = it.starmap(merge_two_lists, segregate_to_groups(mergedLists))
    return mergedLists[0]

def mergeKLists2(lists):
    if not (K:=len(lists)): return None
    mergedLists = lists
    # iterations it takes to merge into 1 List = log(K)
    for _ in range(ceil(log2(K))):
        # merge each sequential parit of group of {mergedLists}
        *mergedLists, = it.starmap(merge_two_lists, segregate_to_groups(mergedLists))
    return mergedLists[0]

    
