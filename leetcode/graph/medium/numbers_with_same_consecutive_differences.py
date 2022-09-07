# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

from typing import List


def numsSameConsecDiff(n: int, k: int) -> List[int]:
    ans = []

    if k == 0:
        return [int(f'{i}'*n) for i in range(1, 10)]  # 111, 222, ...

    #offset = (0,) if k==0 else (-k, +k)
    offset = (-k, +k)
    
    #cache = {}  # digit -> next digit
    
    def dfs(cur): # cur -> list of digits
        if len(cur) == n:
            # convert list of digits to number
            #num = sum(starmap(lambda i, x: 10**i*x, enumerate(reversed(cur))))
            num = int(''.join(map(str, cur)))
            ans.append(num)
            return
            
        for dx in offset:
            cand = cur[-1] + dx # candidate for next digit
            if 0 <= cand < 10:
                cur.append(cand) # Explore
                dfs(cur)
                cur.pop()  # BackTrack
    
    for i in range(1, 10):
        dfs([i])
    
    return ans


def numsSameConsecDiff2(n: int, k: int) -> List[int]:
    numbers = []
    # Backtracking Function
    def process(number, length):
        # If length of number is n, we formed a required number. So, add it
        # numbers list
        if length == n:
            numbers.append(number)
            return
        # For each num in 1 to 9
        for num in range(10):
            # If absolute difference between this num and last digit of
            # number we previously formed is k, we found the next digit
            if abs(number % 10 - num) == k:
                # So, call func with "number*10 + num" number which is of
                # length length+1
                process(number * 10 + num, length + 1)
    
    # Calling process func with first digit as 1 
    for num in range(1, 10):
        process(num, 1)
    
    return numbers