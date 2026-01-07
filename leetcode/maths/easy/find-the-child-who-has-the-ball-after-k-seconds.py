# find-the-child-who-has-the-ball-after-k-seconds

"""
- Each round involves passing ball in particular direction (either left or right)
- direction alternates asa round completes
"""


def numberOfChild(n: int, k: int) -> int:
    # Each round time := n-1
    # passing ball from one end to other end will take n-1 seconds
    rounds_completed, remain_seconds = divmod(k, n - 1)
    if rounds_completed & 1:
        # current round is even hence (Right to Left)
        return n - (remain_seconds + 1)  # +1 as of zero based indexing
    # left to right
    return remain_seconds
