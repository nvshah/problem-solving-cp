# https://leetcode.com/problems/backspace-string-compare/

'''
Que
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

'''

def backspaceCompare(s: str, t: str) -> bool:
    st1 = []
    st2 = []
    
    def prepare(string, stak):
        for c in string:
            if c == '#':
                if stak:
                    stak.pop()
            else:
                stak.append(c)
        
    prepare(s, st1)
    prepare(t, st2)
    
    return ''.join(st1) == ''.join(st2)