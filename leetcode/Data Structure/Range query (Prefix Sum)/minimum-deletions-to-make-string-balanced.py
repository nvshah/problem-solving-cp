# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced

from itertools import accumulate, starmap
from operator import add

'''
Idea 
we will find best mid-point so as to seperate the a & b
Now 
best midpoint = lesser operation on left & right side to remove inferior candidate
'''



class Solution:
    def minimumDeletions(self, s: str) -> int:
        approach2(s)
    

def approach1(s: str) -> int: 
    ''' T.C = O(n) 
        S.C = O(n)
        Idea :- BruteForce
    '''
    N = len(s)
    *a_count_right_reversed, = accumulate(reversed(range(N-1)), lambda count, i: int(s[i+1] == 'a') + count, initial=0)
    a_count_right = reversed(a_count_right_reversed)
    b_count_left = accumulate(range(1, N), lambda count, i: int(s[i-1] == 'b') + count, initial=0)

    operations = starmap(add, zip(b_count_left, a_count_right))
    return min(operations)

def approach2(s: str) -> int: 
    ''' T.C = O(n) 
    '''
    total_a = s.count('a') 
    # determines count of `a` on right side, for given index at moment [i]
    a_count_right = total_a
    # determines count of `b` on left side, for given index at moment [i]
    b_count_left = 0

    min_ops = len(s) # in worst case
    
    for char in s:
        if char == 'a':
            a_count_right -= 1
        
        min_ops = min(min_ops, a_count_right + b_count_left)

        if char == 'b':
            b_count_left += 1
        
    return min_ops

   

if __name__ == '__main__':
    s = Solution()
    s.minimumDeletions("aababbab")

