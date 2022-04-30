# https://leetcode.com/problems/generate-parentheses/

from typing import List


def generateParenthesis(n: int) -> List[str]:
    ans = []
    def generate(o, c, s):
        '''
        DFS
        :param o: total open parenthesis ie '(' available
        :param c: total close parenthesis ie ')' available
        :param s: generated string
        '''
        if not o and not c:  # no open or close parenthesis are available
            ans.append(s)
            return
        
        if o:  # if open parenthesis available
            generate(o-1, c, s+'(')  # add open parenthesis
        
        if c > o:  # if close parenthesis are more than open then only we can include it
            generate(o, c-1, s+')') # add close parenthesis
            
    generate(n,n,'') # initially n open & n close parenthesis are avaialble
    return ans

def generateParenthesis2(n: int) -> List[str]:
    ans = []
    stack = []
    def backtrack(o, c):
        '''
        DFS
        :param o: total open parenthesis ie '(' used
        :param c: total close parenthesis ie ')' used
        '''
        if o == c == n:  # all open & close parenthesis are used
            ans.append(''.join(stack))
            return
        
        if o < n:  # if open parenthesis available
            stack.append('(')  # add
            backtrack(o+1, c)  
            stack.pop()        # remove
        
        if c < o:  # if number of close must be less than open in current stack
            stack.append(')') # add
            backtrack(o, c+1) 
            stack.pop()       # close
            
    backtrack(0,0) # initially n open & n close parenthesis are avaialble
    return ans