# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    """via superset"""
    allowed = set(allowed)
    return len([None for word in words if allowed.issuperset(word)])


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    """via superset"""
    allowed = set(allowed)
    count = len(words)
    for word in words:
        for ch in word:
            if ch not in allowed:
                count -= 1
                break
    return count


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    """via superset"""
    allowed = set(allowed)
    count = len(words)
    for word in words:
        for ch in word:
            if ch not in allowed:
                count -= 1
                break
    return count


def letter_to_number(letter):
    """returns number/position corresponding to letter relative to 'a'"""
    # (ie a:0, b:1, c:2, ... z:25)
    return ord(letter) - ord("a")


def countConsistentStrings_a3(allowed: str, words: List[str]) -> int:
    """via bitmask
    Idea : int is represented via 32 bits & there are 26 characters only
    hence we can use a single number to represent the allowed-characters-set
    """

    def get_bit_mask(letters):
        bit_mask = 0
        for l in letters:
            # identify/associate bit_position
            bit_pos = letter_to_number(l)
            # set that particular bit in bit_mask
            bit_mask |= 1 << bit_pos
        return bit_mask

    allowed_bitmask = get_bit_mask(allowed)
    count = len(words)
    for word in words:
        for ch in word:
            bitpos = letter_to_number(ch)
            # ch in word := iff `bitpos` is set in `allowed_bitmask`
            is_set = (allowed_bitmask & (1 << bitpos)) != 0
            if not is_set:
                count -= 1
                break
    return count


allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
ans = countConsistentStrings_a3(allowed, words)
print(ans)
