# https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack:

    def __init__(self):
        self.cnt = {} # freq-mapping val -> count
        # mapping of stacks where
        # key := freq_cnt, represent the Most Frequent layer
        # value := [stack] Tie at current frequency layer, LIFO removal in case of TIE
        self.stacks = {}

        self.maxCnt = 0 # maxCnt possible among all elem added

    def push(self, val: int) -> None:
        # 1. update freq of {val}
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt

        # 2. update most frequent status layer
        if valCnt > self.maxCnt: # new layer (ie most freq cnt)
            self.maxCnt = valCnt
            self.stacks[valCnt] = [] # add new stack for this new layer (ie new most freq layer)

        # 3. add val to its corresp Most Freq layer
        self.stacks[valCnt].append(val)


    def pop(self) -> int:
        mfs = self.stacks[self.maxCnt] # most frequent stack
        val = mfs.pop()
        self.cnt[val] -= 1  # update {val} freq
        if not mfs: # update new most freq layer
            self.maxCnt -= 1

        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
