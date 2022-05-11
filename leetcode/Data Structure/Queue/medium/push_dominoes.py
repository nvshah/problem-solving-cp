# https://leetcode.com/problems/push-dominoes/
from collections import deque

def pushDominoes(dominoes: str) -> str:
    state = list(dominoes) # result array that will hold final state
    l = len(dominoes)
    
    # 1. push all bending sticks to {que}
    bending_sticks = [i for i in range(l) if dominoes[i] != '.'] 
    que = deque(bending_sticks)
    
    # 2. iterate till que is empty
    while que:
        i = que.popleft()
        d = state[i] 
        if d == 'L':  # left bending stick
            if i > 0 and state[i-1] == '.': 
                # update neighbor state
                state[i-1] = 'L'
                que.append(i-1)
        else:         # right bending stick
            if i+1 < l and state[i+1] == '.':  
                if i+2 < l and state[i+2] == 'L':
                    # here stick {i} will not affect stick {i+1} because of neutralization from stick {i+2}
                    que.popleft()  
                else:
                    # here stick {i+1} will get affected by stick {i} towards right side
                    state[i+1] = 'R'
                    que.append(i+1)
    
    return ''.join(state)