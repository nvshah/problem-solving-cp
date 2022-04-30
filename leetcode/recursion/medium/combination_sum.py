# https://leetcode.com/problems/combination-sum/

'''
Make in change with repeatation allowed
'''

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    '''
        Approach using Pure Recursion not DP
    '''
    ans = []

    def explore(i, nominees, curr_sum):
        '''
            i : pointer to current head starts from left -> right
            nominees : currently selected elements
            curr_sum : sum of all nominees
        '''
        if curr_sum == target:  # found a combination
            ans.append(nominees.copy())
            return
        if (curr_sum > target) or (i == len(candidates)):  # explored all combinations
            return 
        
        # decision 1 :  include i in nominees & explore a combination
        v = candidates[i]
        nominees.append(v)
        explore(i, nominees, curr_sum + v)  # as i is included so curr_sum also changes
        # decision 2 :  exclude i in nominees & explore a combination
        nominees.pop()
        explore(i+1, nominees, curr_sum)

    explore(0, [], 0)
    return ans
    

candidates = [2,3,6,7] 
target = 7  # [[2,2,3],[7]]

candidates = [2,3,5]
target = 8   # [[2,2,2,2],[2,3,3],[3,5]]

candidates = [2]
target = 1  # []

candidates = [1]
target = 1 # [[1]]

candidates = [1]
target = 2  # [[1,1]]

candidates = [1,3,4]
target = 4

ans = combinationSum(candidates, target)
print(ans)