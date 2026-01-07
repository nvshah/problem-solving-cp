# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/


def count_bit(num):
    count = 0
    # 32 bits are used to represent num (assumption)
    for i in range(32):
        count += i & (1 << i)
    return count


def min_bit_flips_to_convert_number(start, goal):
    # T.C = log2(start ^ goal)
    return (start ^ goal).bit_count()
