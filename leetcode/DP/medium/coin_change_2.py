# https://leetcode.com/problems/coin-change-2/

from typing import List


def change(amount: int, coins: List[int]) -> int:
    ''' Using Recursive Memoization '''
    size = len(coins)
    cache = {}
    def dfs(i, amt):
        ''' Gives possible ways to achieve {amount} via {coins[i:]}'''
        if amt == amount:
            return 1
        elif amt > amount:
            return 0 
        if i > size:  # No coins available anymore (all visited)
            return 0
        
        if (i, amt) in cache:
            return cache[(i, amt)]

        # pick & discard coin
        coin = coins[i]
        include_i = dfs(i, amt + coin)  # include
        ignore_i = dfs(i+1, amt)   # exclude

        v = cache[(i, amt)] = include_i + ignore_i
        return v

def change_dp(amount: int, coins: List[int]) -> int:
    ''' Using Recursive Memoization '''
    rows = len(coins)
    cols = amount
    # 1 ;= for getting amoutn =0 we dont require any coins
    dp_matrix = [[1,*[0]*(cols)] for _ in range(rows+1)]

    for i in range(1, rows+1):
        coin = coins[i-1]
        for j in range(1, cols+1):
            if coin > j:
                v = 0
            else:
                left_amt = j - coin 
                v = dp_matrix[i][left_amt]

            dp_matrix[i][j] = v + dp_matrix[i-1][j]

    for r in dp_matrix:
        print(r)

    return dp_matrix[rows][cols]


def change_dp_2(amount: int, coins: List[int]) -> int:
    ''' Using DP space efficient 
        O(n*m) time
        O(n) Space
    '''
    rows = len(coins)
    cols = amount
    # 1 ;= for getting amoutn =0 we dont require any coins
    prev_row = [1,*[0]*(cols)]

    for i in range(1, rows+1):
        curr_row = [1,*[0]*(cols)]

        coin = coins[i-1]
        for j in range(1, cols+1):
            if coin > j:
                v = 0
            else:
                left_amt = j - coin 
                v = curr_row[left_amt]
                
            curr_row[j] = v + prev_row[j]

        prev_row = curr_row

    return prev_row[cols]

print(change_dp_2(5, [1,2,5]))


