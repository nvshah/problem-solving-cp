# https://leetcode.com/problems/power-of-three/submissions/

def isPowerOfThree(n: int) -> bool:
    if n<=0: return False
    if n == 1: return True
    def helper(n):
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return helper(n // 3)
    return helper(n)


a = isPowerOfThree(27)
print(a)
    
