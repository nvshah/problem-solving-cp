class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        ROWS, COLS = m + 1, n + 1

        ascii1 = [ord(c) for c in reversed(s1)]
        ascii2 = [ord(c) for c in reversed(s2)]

        dp = [[-1] * (COLS) for _ in range(ROWS)]

        dp[0][0] = 0  # both are empty strings

        # Fill dummy row and col (first)
        # dummr row
        for j in range(1, COLS):  # accumulate along horizontal axis
            dp[0][j] = dp[0][j - 1] + ascii2[j - 1]  # same as r2 (ie columns values)

        # dummy col
        for i in range(1, ROWS):  # accumulate along vertical axis
            dp[i][0] = dp[i - 1][0] + ascii1[i - 1]  #

        for r in range(1, ROWS):
            i = r - 1  # effective string index (discardinf dummy row offset)
            for c in range(1, COLS):
                j = c - 1  # effective string index (discarding dummy col offset)
                ans = -1
                if ascii1[i] == ascii2[j]:
                    ans = dp[r - 1][c - 1]
                else:
                    ans = min(
                        # r1[i] + r2[j] + dp[m-1][n-1],
                        ascii1[i] + dp[r - 1][c],
                        ascii2[j] + dp[r][c - 1],
                    )
                dp[r][c] = ans

        return dp[-1][-1]
