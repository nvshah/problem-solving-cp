# https://leetcode.com/problems/plus-one/

from typing import List

def plusOne(digits: List[int]) -> List[int]:
    s = len(digits)
    carry = 0
    for i in range(s-1, -1, -1):
        carry, digits[i] = divmod(digits[i] + 1, 10)
        if not carry:
            break 
    else: # carry is still there
        digits.insert(0, 1)
    return digits

def plusOne2(digits: List[int]) -> List[int]:
    s = len(digits)
    digits.reverse()
    carry, i = 1, 0
    while carry:
        if i < s:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
        else:
            digits.append(1) # exhaust all digits & still carry is there
            carry = 0 # to terminate while loop

        i += 1
    return digits[::-1] # undo reverse of begin

a = [1,2,3]
a = [4,3,2,1]
a = [9]
o = plusOne(a)
print(o)
