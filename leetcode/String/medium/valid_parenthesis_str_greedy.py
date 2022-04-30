# https://leetcode.com/problems/valid-parenthesis-string/

def checkValidString(s: str) -> bool:
    # store the count of possible left '(' max & min counts (after negated) uptil now
    leftMin, leftMax = 0, 0

    for c in s:
        if c == '(':
            leftMin, leftMax = leftMin+1, leftMax+1
        elif c == ')':
            if not leftMax: return False  # nothing to negate on left side
            leftMin, leftMax = leftMin-1, leftMax-1
        else: 
            leftMin, leftMax =  leftMin-1, leftMax+1
        
        # if leftMax < 0:
        #     return False 

        if leftMin < 0:
            leftMin = 0

def app2(s):
    l_extra = 0
    r_extra = 0
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if r_extra:
                r_extra -= 1
            elif stack:
                t = stack.pop()
                if t == '*':
                    l_extra += 1
            else:
                return False
        else:
            if stack:
                stack.pop()
                r_extra += 1
            else:
                stack.append('*')
    return not stack or l_extra == len(stack)
