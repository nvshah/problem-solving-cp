class MyStack:
    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)  # push to right (ie TOP)
        
    def pop(self) -> int:
        return self.arr.pop()  # pop from right (ie TOP)

    def peek(self) -> int:
        return self.arr[-1]  # Peek from left (ie Bottom)

    def empty(self) -> bool:
        return not bool(self.arr)
        
    
class MyQueue:

    def __init__(self):
        self.stack = MyStack()

    def push(self, x: int) -> None:
        self.stack.push(x)
        
    def pop(self) -> int:
        stack2 = MyStack()
        while not self.stack.empty():  # go to bottom element with the help of dummy stack2
            stack2.push(self.stack.pop())
        
        val = stack2.pop()
        
        while not stack2.empty():  # Add rest elements again to original stack
            self.stack.push(stack2.pop())
        
        return val
        
    def peek(self) -> int:
        return self.stack.peek()

    def empty(self) -> bool:
        return self.stack.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()