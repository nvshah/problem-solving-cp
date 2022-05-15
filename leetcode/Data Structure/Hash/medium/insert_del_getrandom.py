# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.numsLst = [] # [nums]
        self.numsMap = {} # num -> idx (in numLst)

    def insert(self, val: int) -> bool:
        res = val not in self.numsMap  # we need to insert only the non-existing vals
        if res: # new val
            self.numsLst.append(val)
            self.numsMap[val] = len(self.numsLst)-1 # last idx
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numsMap # can remove only exisitng vals
        if res: # val exists
            idx = self.numsMap[val]
            lastVal = self.numsLst[-1]
            self.numsLst[idx] = lastVal # replace last-val to removed val place
            self.numsMap[lastVal] = idx # update lastVal idx mapping
            self.numsLst.pop()  # remove last pos (ie effectively removed {val})
            del self.numsMap[val] # remove entry for {val}
            
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.numsLst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()