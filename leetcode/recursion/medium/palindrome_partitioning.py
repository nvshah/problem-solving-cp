# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


def isPalindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False 
        l, r = l+1, r-1
    return True


def partition(s: str) -> List[List[str]]:
    res = []
    part = []

    size = len(s)

    def dfs(i):
        '''
         i :- current index for partitioning 
        '''
        if i == size:
            res.append(part.copy())

        for j in range(i, size):
            if isPalindrome(s, i, j):
                part.append(s[i:j+1])
                dfs(j+1)  # search current partiton
                part.pop()

    dfs(0)
    return res

def partition2(s: str) -> List[List[str]]:
    size = len(s)
    ans = []

    def dfs(i,  parts):
        '''
         i :- current index for partitioning 
         return list of partitions
        '''
        if i == size:
            ans.append(parts)
            return

        for j in range(i, size):  # number of parts = size of sub-string at present
            if isPalindrome(s, i, j):
                dfs(j+1, parts + [s[i:j+1]])       # search current partiton

    dfs(0, [])
    return ans

def partition3(s: str) -> List[List[str]]:
    size = len(s)

    def dfs(i,  parts):
        '''
         i :- current index for partitioning 
         return list of partitions
        '''
        if i == size:
            return [parts]
        
        ans = []

        for j in range(i, size):  # number of parts = size of sub-string at present
            if isPalindrome(s, i, j):
                p = dfs(j+1, parts + [s[i:j+1]])       # search current partiton
                ans.extend(p)

        return ans

    return dfs(0, [])


s = "aab"
a = partition3(s)
print(a)


