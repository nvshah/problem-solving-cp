# https://leetcode.com/problems/permutations-ii/

from typing import List
from collections import Counter as ctr 


def permuteUnique(nums: List[int]) -> List[List[int]]:
    '''
        Backtracking & Recursion :- (IDEA) When reach leaf node found 1 permutation
    '''
    ans = []
    curr_permute = []
    size = len(nums)

    # freq = {x:0 for x in nums}
    # for x in nums:
    #     freq[x] += 1

    freq = ctr(nums)

    def dfs():
        '''
            At each leaf node we can find one of possible permutation via backtracking till top level
            NOTE :- Here assume root node = empty string
            so concatenate leaf to root = 1 possible permute

            So All depth level/columns from left -> right will represent unique permutations
        '''
        if len(curr_permute) == size: # found 1 permutaion
            ans.append(curr_permute.copy())

        # At any level there can be atmost m nodes where m = len(freq.keys())
        # ie at any level there can be unique nodes only not reepeating nodes 
        for n in freq:
            if freq[n] > 0: # if we can append node n to next level

                # EXPLORE (Top to Bottom) to explore current depth level/col
                curr_permute.append(n)
                freq[n] -= 1  # decrease freq count as accounted here at current depth

                # solve recursively the currennt depth level/column till reach leaf node
                # As reaching leaf node = goal = find one possible (unique) permutation 
                dfs()  

                # BACKTRACK (Bottom to Up) once current depth/column is explored
                freq[n] += 1  # give back nodes for adjacent depth level exploration
                curr_permute.pop() # empty the curr ans list to track node of adjacent depth level
    dfs()
    return ans

nums = [1,1,2]
print(permuteUnique(nums))

nums = [1,2,3]
print(permuteUnique(nums))




