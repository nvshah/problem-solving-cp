# https://leetcode.com/problems/operations-on-tree/

from collections import defaultdict, deque
from typing import List 

''' Concepts : BFS | Map '''

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [None]*len(parent)
        self.child = defaultdict(list)  # parent -> child_indexes
        for i, p in enumerate(parent):
            self.child[p].append(i)   # parent -> child
        
        print(self.child)
        
    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]: return False # lock already acquired
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        #if not self.locked[num]: return False # not locked
        if self.locked[num] != user: return False # diff user
        self.locked[num] = None # unlock
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num]: return False
        # check ancestors
        cur = num
        while cur != -1:
            if self.locked[cur]: return False  # must not be locked
            cur = self.parent[cur]
        
        hasLocks = 0 # locked cnts for desscendants
        q = deque([num])  # queue
        # look for descendents using BFS (ie Level by level)
        while q:
            n = q.popleft()
            if self.locked[n]:  # detected 1 locked descendents
                self.locked[n] = None
                q.extend(self.child[n])
                break
            q.extend(self.child[n])
        else:
            return False
        
        # Simple BFS traversal to make all descendents unlock
        while q:
            n = q.popleft()
            self.locked[n] = None
            q.extend(self.child[n])
        
        # locks the given node 
        self.locked[num] = user
        
        return True
            


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)