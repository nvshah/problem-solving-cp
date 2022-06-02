# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

def removeDuplicates(self, s: str, k: int) -> str:
    # elem -> (char, count)
    stack = [['$', -1]]  # dummy member
    
    for c in s:
        if c == stack[-1][0]:
            stack[-1][1] += 1  # consider consecutive char
        else:
            stack.append([c, 1])  # add new non-consecutive character
            
        if stack[-1][1] == k:
            stack.pop()
    
    # ctr = Counter(dict(stack[1:]))
    # *elms, = ctr.elements()
    # return ''.join(elms)
    
    # join all the characters back
    res = []
    for char, cnt in stack[1:]:
        res.append(char*cnt)
    return "".join(res)