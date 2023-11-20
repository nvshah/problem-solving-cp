# https://leetcode.com/problems/validate-stack-sequences/
from typing import List 

def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    i = 0  # pooped pointer
    iLimit = len(popped)
    for n in pushed:
        stack.append(n)

        # pop operation
        while stack and i < iLimit and stack[-1] == popped[i]:
            stack.pop()
            i += 1
        
    return stack == []
        
def validateStackSequences2(pushed: List[int], popped: List[int]) -> bool:
    stack = []

    while popped or pushed:
        if popped:
            if stack and stack[-1] == popped[0]:
                popped.pop(0)
                stack.pop()
                continue
            elif not pushed:
                return False 
        if pushed:
            stack.append(pushed.pop(0))
    
    return stack == []
            
                
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
popped = [4,3,5,1,2]
ans = validateStackSequences2(pushed, popped)
print(ans)