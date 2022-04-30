# https://leetcode.com/problems/permutations/submissions/

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    '''
    Find permutations without needs of backtracking (only Explore)
    Keep track of processed & unprocessed parts from starting (ie Top-Down)
    so at the end processed part will be one of possible ans when unprocessed part is empty
    '''
    ans = []

    def explore(p, up):
        '''
        explore the permutation of p with up
        IDEA :- Go element by element at each index as level progress
        :param p: processed part
        :param up: unprocessed part
        :return: one of possible permute ( combining processed & unprocessed part )
        '''
        if not up:
            ans.append(p)
            return
        # draw first element from unprocessed at each level
        new_e = up[0]
        # number of slots available (in processed part)
        # so that new_e can be put into processed part
        slots_available = len(p) + 1
        for i in range(slots_available):  # slots to be fill
            new_p = [*p[:i], new_e, *p[i:]]
            # as first character is drawn from unprocessed at each level
            new_up = up[1:]
            explore(new_p, new_up)
    explore([], nums)
    return ans

def permute_dfs(arr):
    ''' Find Permutation via Explore & BackTrack '''
    t = []  # list that holds current permute
    ans = []  # list of all permutes
    size = len(arr)
    available = [1]*size # to check which element are available currently to create a single permute

    def dfs():
        if len(t) == size:
            ans.append(t.copy())
            return

        for i in range(size):
            if available[i]:
                # EXPLORE -----
                t.append(arr[i])
                available[i] = 0
                dfs()
                # BACKTRACK -----
                available[i] = 1
                t.pop()
    dfs()
    return ans