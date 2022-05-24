# https://leetcode.com/problems/longest-valid-parentheses/

''' Via Stack '''
def longestValidParentheses(s: str) -> int:
    # stk is stack that will hold the incomplete '(' index
    stk = [-1]  # -1 representing standing before the 1st idx (ie 0)
    res = 0 # longest possible valid substr
    for i, c in enumerate(s):
        if c == '(':
            stk.append(i)
        else:
            stk.pop()
            # there must be atleast 1 '(' present in stack
            if not stk:   # invalid substring
                # new start mark point ie end of ')'
                stk.append(i)
            else:    
                # check the length of (valid) substring
                lnth = i - stk[-1]  # length of possible valid substring
                res = max(res, lnth) 
    
    return res

s = "(()"
s = ")()())"
a = longestValidParentheses(s)

print(a)
