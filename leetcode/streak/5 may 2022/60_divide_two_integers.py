# https://leetcode.com/problems/divide-two-integers/submissions/

def divide(dividend: int, divisor: int) -> int:
    q = 0  # quotient
    a, b = abs(dividend), abs(divisor)  # a/b
    while a >= b:
        # Exponential reach out
        tmp = b
        mult = 1  # multiplier to tmp (ie mult * tmp = cur divisor)
        while a >= tmp:
            a -= tmp  # division & remainder
            q += mult  # current quotient
            mult += mult  # exponential increase in divisor val
            tmp += tmp  # 
        
    if (dividend >= 0 and divisor < 0) or (divisor > 0 and dividend <= 0):
        q = -q
            
    m = 2**31
    
    ans = max(-m, min(m-1, q))
    
    return ans

a = divide(7, -3)
print(a)
