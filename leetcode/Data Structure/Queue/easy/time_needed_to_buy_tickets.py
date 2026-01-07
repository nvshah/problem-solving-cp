from typing import List


def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    time = 0
    for idx, count in enumerate(tickets):
        if count == 0:
            continue
        tickets[idx] -= 1
        time += 1
        if idx == k and tickets[idx] == 0:
            return time
    return time


def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    time = 0
    for idx, count in enumerate(tickets):
        if idx <= k:
            time += min(tickets[idx], tickets[k])
        es
