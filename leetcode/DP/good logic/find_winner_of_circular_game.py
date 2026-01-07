# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

from collections import deque


def findTheWinner1(n: int, k: int) -> int:
    """Via Deque"""
    que = deque(range(1, n + 1))

    while len(que) > 1:
        for _ in range(k - 1):
            # move all element before the target to end of que
            que.append(que.popleft())
        # remove target
        que.popleft()

    return que[0]


def findTheWinner1(n: int, k: int) -> int:
    """Via Recursion (ie Top Down DP)

    Reverse Engineering

    We know that winner will remain So position corresponding to winner can be deduced for previous round
    Position for any element in next round will be
        if cur_pos - k if -ve then (n-k) is new position
           cur_pos - k if +ve
    Now We need to do Reverse Engineering i.e Find position in previous round
    cur_round + k  // as prev -> next we are subtracting so next -> prev we will add

    NOTE: while moving from prev -> next candidates is lesser in next so index will be in bound
    but while moving from next -> prev candidates is more in prev so it can result in index which will be out of bound

    So moving from next -> prev

    (cur_round + k) % cardinality_prev_round
    """

    def helper(size):
        """return the index/position of winner in current round with `size` of candidates
        param: size: total candidates in current round
        """
        if size == 1:
            # Last round with only winner left at position 0
            return 0
        winner_pos_in_next_round = helper(size - 1)
        winner_pos_in_cur_round = (winner_pos_in_next_round + k) % size
        return winner_pos_in_cur_round

    winner_pos = helper(n)
    winner_val = winner_pos + 1
    return winner_val
