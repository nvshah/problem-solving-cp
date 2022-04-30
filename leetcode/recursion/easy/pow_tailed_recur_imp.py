# https://leetcode.com/problems/powx-n/

def myPow(x: float, n: int) -> float:
    '''
    Approach :- using Recurrsion (Divide & Conquer)
    T.C :- logarithmic (log(n))

    NOTE :- pow() & log() are correlated to each other (probably inverse of each other)
    '''
    def helper(x, n):
        if x == 0: return 0
        if n == 0: return 1
        if n == 1: return x 

        q, r = divmod(n, 2)

        half = myPow(x, q)  # calc half 

        # in case if remainder left (ie one x is yet left to be multiplied)
        # eg 3^5 = 3 * 3^4 * 3^4
        return x*half*half if r else half*half
        
    x_to_n = helper(x, abs(n))
    return x_to_n if n >= 0 else 1 / x_to_n

ans = myPow(2, 5)
print(ans)
    