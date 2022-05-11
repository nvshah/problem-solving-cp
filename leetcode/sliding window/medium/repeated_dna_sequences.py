# https://leetcode.com/problems/repeated-dna-sequences/
from typing import List

'''
Que :
Given a string s that represents a DNA sequence, 
return all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule. You may return the answer in any order.
'''

'''
Concepts :- {Set, Sliding Window, Map}
'''

'''Idea :- Sliding Window '''
def findRepeatedDnaSequences(s: str) -> List[str]:
    seen, res = set(), set()
    
    for i in range(len(s)-9):
        sub = s[i:i+10]
        if sub in seen:  # substring occuring more than 1 time
            res.add(sub)
        seen.add(sub)  # registry 
        
    return res