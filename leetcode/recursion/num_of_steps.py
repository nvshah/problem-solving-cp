# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def numberOfSteps(num: int) -> int:
    ''' In one step, if the current number is even, 
    you have to divide it by 2, otherwise, you have to subtract 1 from it.'''
    def helper(n, totalSteps):
        if n == 0:
            return totalSteps
        n = n // 2 if n % 2 == 0 else n-1
        return helper(n, totalSteps+1)
    return helper(num, 0)

n = 14
n = 8
n = 123
ans = numberOfSteps(n)

print(ans)