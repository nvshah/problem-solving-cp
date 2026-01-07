# https://www.geeksforgeeks.org/find-xor-of-numbers-from-the-range-l-r/


"""
Try to find pattern 
[1, 1] -> 1
[1, 2] -> 3
[1, 3] -> 0 
[1, 4] -> 4 

[1, 5] -> 1
[1, 6] -> 7
[1, 7] -> 0 
[1, 8] -> 8 

[1, 9] -> 1
[1, 10] -> 11 
[1, 11] -> 0 
[1, 12] -> 12

------
n % 4 == 0 -> XOR(1 to n) = n
n % 4 == 1 -> XOR(1 to n) = 1
n % 4 == 2 -> XOR(1 to n) = n + 1
n % 4 == 3 -> XOR(1 to n) = 0

XOR(L to R) = XOR(1 to R) ^ XOR(1 to L-1)

"""


def xor_upto(n):
    """find xor of all numbers from 1 -> n
    T.C = O(1)
    S.C = O(1)
    """
    match n % 4:
        case 0:
            return n
        case 1:
            return 1
        case 2:
            return n + 1
        case 3:
            return 0


# def xor_upto(n):
#     if n % 4 == 0:
#         return n
#     elif n % 4 == 1:
#         return 1
#     elif n % 4 == 2:
#         return n + 1
#     else:
#         return 0


def xor_range(l, r):
    """find xor of all numbers from l -> r (both inclusive)
    T.C = O(1)
    S.C = O(1)
    """
    return xor_upto(r) ^ xor_upto(l - 1)


ans = xor_range(3, 98)
print(ans)
