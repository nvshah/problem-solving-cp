# https://leetcode.com/problems/reverse-bits/

def reverseBits(n: int) -> int:
    #num = int(bin(n)[2:].zfill(0)[::-1], 2)
    num = int(f'{n:032b}'[::-1], 2)
    return num

def reverseBits2(n: int) -> int:
    res = 0
    # 1 calculate from RHS evry bit
    for i in range(32):
        bit = (n >> i) & 1 # shift number by 
        res = res | (bit << (31-i))  # place calculated bit at LHS

    return res



b = '00000010100101000001111010011100'
n = int(b, 2)
ans = reverseBits2(n)
print(ans)



