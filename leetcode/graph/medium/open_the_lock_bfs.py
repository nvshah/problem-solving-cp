# https://leetcode.com/problems/open-the-lock/submissions/

from collections import deque
from typing import List


def openLock(deadends: List[str], target: str) -> int:
    ends = set(deadends)
    if "0000" in ends: return -1 # impossible
    
    def getPermute(s): # s -> current pattern (code) in lock
        *digits, = map(int, s)
        permuts = []
        for i in range(4):
            up = (digits[i] + 1) % 10  # scroll up
            down = (digits[i] - 1 + 10) % 10 # scroll down
            
            p = [*s]
            for w in (up, down):
                p[i] = str(w)
                permuts.append(''.join(p))
        
        return permuts
    
    # BFS
    que = deque([('0000', 0)]) # (code, cnt)
    visited = ends  # we dont want to visit deadends
    visited.add('0000')
    while que:
        code, cnt = que.popleft()
        if code == target: return cnt
        
        # Get all possible permutations of code after 1 change
        children = getPermute(code)
        cnt += 1
        for c in children:
            if c not in visited:
                visited.add(c) # mark visit
                que.append((c, cnt))
        
    return -1

deadends = ["8888"]
target = "0009"
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
ans = openLock(deadends, target) 
print(ans)