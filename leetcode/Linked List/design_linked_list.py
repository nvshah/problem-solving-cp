# https://leetcode.com/problems/design-linked-list/submissions/

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    '''Doubly Linked List'''

    def __init__(self):
        # create 2 dummy nodes
        self.start = Node(-1)
        self.end = Node(-1)
        self.start.next, self.end.prev = self.end, self.start
        
    def adjustPointers(self, node, prev, nxt):
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, index: int) -> int:
        cur = self.start.next
        toSkip = index
        while toSkip and cur:
            cur = cur.next
            toSkip -= 1
        
        if (toSkip != 0) or (cur in [self.end, None]):  # index out of range
            return -1
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        n = Node(val)
        self.adjustPointers(n, self.start, self.start.next)
        
    def addAtTail(self, val: int) -> None:
        n = Node(val)
        self.adjustPointers(n, self.end.prev, self.end)

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.start.next
        toSkip = index
        while toSkip and cur:
            cur = cur.next
            toSkip -= 1
        
        # index out of bound
        if (toSkip != 0) or (cur == None): return
        
        n = Node(val)
        self.adjustPointers(n, cur.prev, cur)

    def deleteAtIndex(self, index: int) -> None:
        cur = self.start.next
        toSkip = index
        while toSkip and cur:
            cur = cur.next
            toSkip -= 1
        
        # index out of bound
        if (toSkip != 0) or (cur in [self.end, None]): return
        
        cur.prev.next, cur.next.prev = cur.next, cur.prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)