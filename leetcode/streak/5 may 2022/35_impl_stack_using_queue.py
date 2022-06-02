# https://leetcode.com/problems/implement-stack-using-queues

class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x) # add from right side (Queue - FIFO)

    def pop(self) -> int:
        size = len(self.queue)   
        for i in range(size-1):  # Shift current top node to the left-most side
            self.queue.append(self.queue.pop(0))  # remove from left & add to right
        return self.queue.pop(0) # remove from left side (Queue - FIFO)

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not bool(self.queue)    
    

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()