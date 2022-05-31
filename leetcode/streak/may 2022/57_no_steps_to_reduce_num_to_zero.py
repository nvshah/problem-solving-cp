# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def numberOfSteps(num: int) -> int:
    def helper(n, totalSteps):
        if n == 0:
            return totalSteps
        n = n // 2 if n % 2 == 0 else n-1
        return helper(n, totalSteps+1)
    return helper(num, 0)