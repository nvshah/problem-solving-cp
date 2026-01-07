# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        open_brackets_pos = []  # loc of open brackets (non-editable)
        proxies_pos = []  # loc of places (editable)

        for i in range(len(s)):
            bracket, code = s[i], locked[i]
            if code == '0':
                proxies_pos.append(i)
                continue

            if bracket == '(':
                open_brackets_pos.append(i)
                continue

            if open_brackets_pos:
                open_brackets_pos.pop()
                continue

            if proxies_pos:
                proxies_pos.pop()
                continue

            return False

        while open_brackets_pos and proxies_pos:
            if open_brackets_pos[-1] > proxies_pos[-1]:
                # no close bracket ahead of last open bracket
                return False
            open_brackets_pos.pop()
            proxies_pos.pop()

        # At last there should be no open brackets and even length proxies (ie editable places)
        return len(open_brackets_pos) == 0 and len(proxies_pos) % 2 == 0