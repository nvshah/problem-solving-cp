# https://leetcode.com/problems/unique-binary-search-trees/

from math import comb

def numTrees(n: int) -> int:
    return comb(2*n, n) // (n+1)


def numTrees_dp(n: int) -> int:
    # number of Trees possible with {i} nodes where i is the index of array
    numTrees = [0] * (n+1)  # dp

    numTrees[0] = 1  # to accomodate formula make it 1 
    numTrees[1] = 1  # with 1 node 1 tree is possible

    for nodes in range(2, n+1):
        # curr nodes cnt = {nodes}
        for root in range(1, nodes+1):
            left = root - 1       # left sub tree
            right = nodes - root  # right sub tree
            numTrees[nodes] += numTrees[left] * numTrees[right]

    return numTrees[n]