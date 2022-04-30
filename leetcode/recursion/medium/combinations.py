# https://leetcode.com/problems/combinations/

from typing import List
import itertools


def combine(n: int, k: int) -> List[List[int]]:
    return itertools.combinations(range(1,n+1), k)

def combine2(n: int, k: int) -> List[List[int]]:
    '''
    T.C = k * n^k  // k for cloning & n^k as depth of tree
    '''
    def find(n, k, comb):
        if k == 0:
            return [comb.copy()]
        
        ans = []
        for i in range(n, 0, -1):
            #comb.append(i)
            ans.extend(find(i+1, k-1, comb + [i]))
            #comb.pop()
        
        return ans

    return find(n, k, [])

def combine3(n: int, k: int) -> List[List[int]]:
    '''
    T.C = k * n^k  // k for cloning & n^k as depth of tree
    '''
    ans = []
    def backtrack(s, comb):
        if len(comb) == k: # found one of the combination
            ans.append(comb.copy())
            return

        for i in range(s, n+1):
            comb.append(i)     # take {i} as the participant
            backtrack(i+1, comb)  # Explore ahead
            comb.pop()         # remove {i} as the participant
        
        return ans

    return backtrack(1, [])  

def combine4(n: int, k: int) -> List[List[int]]:
    '''
    T.C = k * n^k  // k for cloning & n^k as depth of tree
    '''
    ans = []
    comb = []
    def dfs(i):
        if len(comb) == k:
            ans.append(comb.copy())
            return

        if i == n+1:
            return
        
        # pick i 
        comb.append(i)
        dfs(i+1)

        comb.pop()
        # Unpick i
        dfs(i+1)

    dfs(1)
    return ans

#print(combine2(4, 2))

print(combine4(4,2))
