import heapq as hq
from math import prod

def soln():
    # number of employees making donations
    q = eval(input())
    # donations of [q] employees
    *donations, = map(int, input().split())
    # company looking to target [p] employees for its donation amount
    p = int(input())

    # least [p] donations to target by company
    hq.heapify(donations)

    # company donations = multiplications of least [p] donations done by employees !
    return prod(hq.heappop(donations) for _ in range(p))


if __name__ == '__main__':
    a = soln()
    print(a)