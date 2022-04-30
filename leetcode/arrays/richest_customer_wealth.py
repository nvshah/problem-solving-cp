from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    return max(map(sum, accounts))

if __name__ == '__main__':
    print(maximumWealth([[1,5], [7,3], [3,5]]))