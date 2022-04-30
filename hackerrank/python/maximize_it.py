# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as it

# Que : https://www.hackerrank.com/challenges/maximize-it/problem


def squaresum(r: tuple) -> int:
    return sum([i**2 for i in r])


k, m = map(int, input().split())
ans = -1

cl = [sorted(set(map(int, input().split())), reverse=True) for _ in range(k)]
# as small size list elements have higher chances to be in answer than large sized lists
cl.sort(key=lambda l: len(l))

for b in it.product(*cl):
    s = squaresum(b)
    # Once it is less than m it will never raise more than m
    if s < m:
        if s > ans:
            ans = s
        break        # As s from now onwards will always be less than this value & also it will be less than m
    else:
        mod = s % m
        if mod == m-1:
            ans = mod   # Max Value is reached
            break
        else:
            ans = mod if mod > ans else ans

print(b)
print(ans)
