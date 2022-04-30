class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <= 0: return False
        # return log2(n) % 1 == 0
        
        if n == 0:
            return False
        return (n & n-1) == 0