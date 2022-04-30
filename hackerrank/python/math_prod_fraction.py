from fractions import Fraction
from functools import reduce
from math import prod
import operator as op


def product(fracs):
    #t = prod(fracs)
    t = reduce(op.mul, fracs, initial=1)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

    # f1 = Fraction(1, 2)
    # f2 = Fraction(3, 9)

    # f3 = f1*f2
    # print(f3)
