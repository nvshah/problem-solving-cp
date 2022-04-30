# https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    stack = []
    m = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in m:   
            if stack:
                if m[c] != stack.pop(): return False
            else:
                return False
        else:
            stack.append(c)
    return not bool(stack)