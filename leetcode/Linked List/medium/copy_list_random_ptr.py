# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    copyMap = {None:None}  # none for empty node

    curr = head

    # 1. Copy all nodes 
    while curr:
        copyMap[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    # 2. Link Pointers 
    while curr:
        copyNode = copyMap[curr]
        copyNode.next = copyMap[curr.next]
        copyNode.random = copyMap[curr.random]
    
    return copyMap[head]
