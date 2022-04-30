# https://leetcode.com/problems/design-circular-queue/

class Node:
    def __init__(self, val, nxt, prev):
        self.val, self.nxt, self.prev = val, nxt, prev

class MyCircularQueue:

    def __init__(self, k: int):
        #self.size = k  # max size of Queue
        self.space = k # initially all slots are empty // space := empty slots
        self.left = Node(-1, None, None) # dummy node at start
        self.right = Node(-1, None, self.left) # dummy node ar end
        self.left.nxt = self.right # link left & right Nodes

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False # no empty slots
        cur = Node(value, self.right, self.right.prev)
        # disconnect the rear node
        self.right.prev.nxt = cur  # rear -> cur
        self.right.prev = cur  # cur -> right
        self.space -= 1  # empty slots updates 
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False # No Node to pop
        self.left.nxt = self.left.nxt.nxt # left -> newFront  // ie newFront = (ie 2nd node from left)
        self.left.nxt.prev = self.left    # left <- newFront  // BiDirectional Mapping
        self.space += 1  # new slot freed up
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.nxt.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.nxt == self.right
        
    def isFull(self) -> bool:
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()