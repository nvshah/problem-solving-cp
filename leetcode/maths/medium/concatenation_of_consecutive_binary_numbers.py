# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

def concatenatedBinary(n: int) -> int:
    num = 1
    for i in range(2, n+1):
        # For every new num : its bits gonna appeneded at the RHS
        # Thus current (resulted) bits gonna shift on left side by the offset = (bit cnt of new num {i}) 
        # left shift = multiply by 2
        num = ((num << i.bit_length()) + i) % (10**9 + 7)
    return num

concatenatedBinary(3)  # 27