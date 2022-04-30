import itertools as it

# Que -> https://www.hackerrank.com/challenges/map-and-lambda-expression/problem


def cube(x): return pow(x, 3)


def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    second_last = 0

    def getNextAndTraceLast(last, _):
        nonlocal second_last
        next = last + second_last
        second_last = last
        return next

    return it.chain((0,), it.accumulate([1, *([0]*(n-2))], getNextAndTraceLast))

    # return list(
    #     it.accumulate([0, 1, *[0]*(length-2)],
    #                   lambda x, y: [locals().update(lv=x), x+y][2])
    # )


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
