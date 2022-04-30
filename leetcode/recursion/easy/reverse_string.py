# https://leetcode.com/problems/reverse-string/

from typing import List


def reverseString(s: List[str]) -> None:
    ''' Reverse String Inplace using Recurrsion '''
    if not s: return
    l = len(s)
    q = l // 2
    m = q-1
    def swapper(i):
        if i > m:  # swapped all the elements till middle
            return 
        # swap
        s[i], s[-i-1] = s[-i-1], s[i]
        swapper(i+1) # look for another swap
    swapper(0)

if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    s = ["H","a","n","n","a","h"]
    s = ['a']
    reverseString(s)
    print(s)