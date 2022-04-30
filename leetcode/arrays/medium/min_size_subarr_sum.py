# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List

def minSubArrayLen2(target: int, nums: List[int]) -> int:
    l = u = 0   # lower & upper bound to point the window that include nums s.t sum >= target
    res = len(nums)+1  # minimal number of connsecutive nums
    extra = 0    # extra sum for curr window on top of target value
    currSum = 0  # sum of current window [l, u]
    gat = 0      # sum of gathered consecutive numbers out of window so that may be included in future

    size = len(nums)

    for r in range(size):
        if nums[r] >= target:  # Single number 
            return 1
        
        tSum = currSum + nums[r] 
        
        if tSum >= target:
            extra = tSum - target   # {extra} which can be removed from left side
            if extra:
                pre = nums[l]       # prefix sum   
                ful = extra + gat   # max-amt that can be removed from current window
                i = 0
                while pre <= ful:   # removing as much prefix as possible !
                    i += 1
                    pre += nums[l+i]
                if i > 0:           # if removed any prefix
                    pre -= nums[l+i] # negate sentinel prefix val (ie {l+i} index value should not be accounted in prefix Sum)
                    #currSum = currSum - pre + ful - extra
                    #currSum = currSum - pre + gat + nums[r]
                    currSum = tSum - pre + gat
                    l, u = l+i, r
                    gat = 0
                else:               # no prefix were removed so 
                    if currSum >= target:  # contribute curr num to gathered sum so that it can help to remove prefix in future
                        gat += nums[r]
                    else:
                        currSum = tSum  # include curr num at {r} in current sum
                        u = r
            else:
                currSum += nums[r]
                u = r

            res = min(res, u-l+1)
        else:
            currSum += nums[r]
            u = r


    # if currSum >= target:
    #     extra = currSum - target 
    #     pre = nums[l]
    #     ful = extra + nums[r] + gat
    #     i = 0
    #     while pre <= ful:
    #         i += 1
    #         pre += nums[l+i]
    #     if i > 0:
    #         pre -= nums[l+i]
    #         currSum = currSum - pre + ful - extra
    #         l, u = l+i, r
    #         gat = 0
    #     else:
    #         gat += nums[r]

           

    print(currSum, l, u)
    return res % (len(nums)+1)

def minSubArrayLen(target: int, nums: List[int]) -> int:
    ''' 
    Idea :- Expand & Shrink Sliding Window
    ''' 
    l = 0   # left pointer of window
    size = len(nums)
    currSum = 0  # current sum of window [l, r]
    res = size+1  # minimal cnt of window

    for r in range(size):   # Grow window 1 step at time
        if nums[r] >= target:  # Single number (Edge Case)
            return 1

        currSum += nums[r]

        while currSum >= target:  # Shrink window as much as possible
            # Found 1 possible Window [l, r] so Jot down that at moment
            res = min(res, r-l+1)
            # Try to reduce the window Size (Greedy) from left side
            currSum, l = currSum - nums[l], l+1

    return res % (size+1)

target = 7
nums = [2,3,1,2,4,3]

#target = 4
#nums = [1,4,4]

#target = 11
#nums = [1,1,1,1,1,1,1,1]

target = 11
nums = [1,2,3,4,5]

target = 15

target = 7
nums = [2,3,1,5,4,3,2,3]

target = 15
nums = [2, 14]
ans = minSubArrayLen(target, nums)
print(ans)