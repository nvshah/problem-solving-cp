# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, k, v) -> None:
        self.key, self.val = k, v 
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.map = {}  # map for key -> Node

        # left -> LRU
        # right -> MRU
        self.left, self.right = Node(0,0), Node(0,0)

        # Doubly Linked List (left -> head, right -> tail)
        self.left.next, self.right.prev = self.right, self.left

        # * This any node we put will always be in between left & right (boundaries)
    
    # remove {node} from doubly linked list
    def remove(self, node):
        # node will always gonna be middle node & not boundary one 
        prev, next = node.prev, node.next 
        prev.next, next.prev = next, prev  # removed {node} from doubly-list


    # insert {node} at the end(ie right side)
    def append(self, node):
        mru = self.right.prev    # mru (most recently used) = last {node} putted
        node.prev, node.next = mru, self.right # add {node} in between {mru} & {right}  (ie at last)
        mru.next = self.right.prev = node      # adjust existsing nodes ptrs

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            # Update the LRU/MRU Tracking status for {node}
            self.remove(node)
            self.append(node)
            
            return node.val
        return -1  # node not found in LRU cache
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # remove old {node} from doubly-list
            self.remove(self.map[key])

        node = Node(key, value)
        # 1. add {key} -> {node} in {map}
        self.map[key] = node 
        # 2. add new {node} into doubly-list 
        self.append(node)

        # check capacity constraints
        if len(self.map) > self.capacity:
            # remove the LRU node from 
            # 1. doubly_linked_list (ie from left side) 
            # 2. & {map} as well

            lru = self.left.next  # least recently used node
            self.remove(lru)      # remove from doubly-list
            del self.map[lru.key]     # remove from map


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)