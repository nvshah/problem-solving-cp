# https://leetcode.com/problems/design-hashmap/

# Simple Soln 1 --- O(1)

class MyHashMap1:

    def __init__(self):
        self.l = [-1]*(1000001)

    def put(self, key: int, value: int) -> None:
        self.l[key] = value      

    def get(self, key: int) -> int:
        return self.l[key]
            
    def remove(self, key: int) -> None:
        self.l[key] = -1


# Attempt 2 ---- (CHAIN | Bucket Approachs)

class MyHashMap:

    def __init__(self):
        # ! consider taking large prime num to get good hashing reesult
        self.size = 500  # ! - val is concluded after several trial checks
        self.buckets = [[] for _ in range(self.size)]
    
    def get_hash(self, key):
        return key % self.size
    
    def get_bucket(self, key):
        h = self.get_hash(key)
        return self.buckets[h]

    def put(self, key: int, value: int) -> None:
        bucket = self.get_bucket(key)
        for i, t in enumerate(bucket):
            if t[0] == key:
                t[1] = value  # Update value
                return
        bucket.append([key, value])  # New key
            
    def get(self, key: int) -> int:
        bucket = self.get_bucket(key)
        for k, v in bucket:
            if k == key:
                return v
        return -1
            
    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)
        for i, t in enumerate(bucket):
            if t[0] == key:
                del bucket[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)