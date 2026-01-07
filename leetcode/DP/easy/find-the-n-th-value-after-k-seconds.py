# find-the-n-th-value-after-k-seconds
"""
Bottom Up DP | Tabular Way
"""


def valueAfterKSeconds(n: int, k: int) -> int:
    """Linear DP"""
    dp = [1] * n
    for _ in range(k):
        for i in range(1, n):
            # in place modification as it relies just on prev value
            dp[i] = dp[i - 1] + dp[i]
    return dp[n - 1] % (10**9 + 7)
