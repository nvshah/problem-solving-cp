# https://leetcode.com/problems/integer-to-roman/

'''
Constraints
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
'''

def intToRoman(num: int) -> str:
    symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M' ]
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    res = []
    # s -> symbol, v -> val
    for s, v in reversed((*zip(symbols, values),)):
        if num // v:
            d, r = divmod(num, v)
            res.append(s * d)   # symbol {s} will repeat {d} times
            num = r  # remmainig {r} will be looked ahead
    return ''.join(res)


num = 3
num = 9
roman = intToRoman(num)
print(roman)