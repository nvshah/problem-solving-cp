# https://leetcode.com/problems/lfu-cache/
from collections import defaultdict

class ListNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right    

class LinkedList:
    '''Double Ended Linked List for LRU Cache
        Operations: push-right, pop-left, remove-val
    '''
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1) 
        self.head.right = self.tail
        self.tail.left = self.head
        self.map = {}  # Value -> ListNode

    @property
    def length(self):
        return len(self.map)
    
    def append(self, val):
        '''Add [val] to right end'''
        last = self.tail.left
        node = ListNode(val, right=self.tail, left=last)
        self.map[val] = node 
        self.tail.left = node # update right
        last.right = node # update left
    
    def remove(self, val):
        if val not in self.map: return 

        node = self.map[val] 
        prev, nxt = node.left, node.right 
        prev.right, nxt.left = nxt, prev
        del self.map[val] 

    def popLeft(self):
        if not self.map: return 

        val = self.head.right.val 
        self.remove(val) 
        return val
    
    def __str__(self) -> str:
        res = []
        ptr = self.head.right
        while ptr.right != self.tail:
            res.append(ptr.val)
        
        return '->'.join(res)
    
    def __repr__(self) -> str:
        res = []
        ptr = self.head.right
        while ptr != self.tail:
            res.append(ptr.val)
            ptr = ptr.right
        
        return str(res)

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.countMap = defaultdict(int)  # key -> count
        self.listMap = defaultdict(LinkedList) # count -> LinkedList[keys] //for LRU cache
        self.valueMap = {} # Key -> val
        self.lfuCount = 1  # used to create space via removing node from List, when capacity is full

    # PRotocols --> 

    def get(self, key: int) -> int:
        val = self.valueMap.get(key, -1)
        if val != -1:
            self.updateCount(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key not in self.valueMap and len(self.valueMap) == self.capacity:
            # need to invalidate (ie empty some space)
            self.invalidate()
        self.valueMap[key] = value 
        self.updateCount(key)
    
    # HElpers --> 

    def invalidate(self):
        removedKey = self.listMap[self.lfuCount].popLeft() # invalidate
        del self.valueMap[removedKey] 
        del self.countMap[removedKey] 
         
    def updateCount(self, key):
        count = self.countMap[key]
        newCount = count + 1
        # transfer [key] from count -> count+1
        if count:
            self.listMap[count].remove(key) 
            if self.lfuCount == count and self.listMap[count].length == 0:
                self.lfuCount = newCount
        else: 
            self.lfuCount = 1

        self.listMap[newCount].append(key) # transfer
        
        # update frequency
        self.countMap[key] = newCount


## -- TEST

#lfu = LFUCache(2)

# def printDebug():
#     print('---')
#     print(lfu.listMap)
#     print(lfu.countMap)
#     print(lfu.valueMap)
#     print(lfu.lfuCount)
#     print('---')

# lfu.put(1, 1) 
# lfu.put(2, 2) 
# #printDebug()
# print(lfu.get(1))
# #printDebug()
# lfu.put(3, 3)
# #printDebug()
# print(lfu.get(2))
# print(lfu.get(3))
# #printDebug()
# lfu.put(4, 4) 
# printDebug()
# print(lfu.get(1))
# print(lfu.get(3))
# print(lfu.get(4))
#printDebug()
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)