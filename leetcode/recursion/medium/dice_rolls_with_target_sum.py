# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

def numRollsToTarget(d: int, f: int, target: int) -> int:
        ways = [0]
        #p = []
        def helper(t, d):
            #print(t,d)
            if (t == 0) and (d == 0):
                #print(p)
                ways[0] += 1
                return
            if t == 0 or d == 0:
                return
            u = min(f, t)
            for j in range(1, u+1):
                #p.append(j)
                helper(t-j, d-1)
                #p.pop()
        helper(target, d)
        return ways[0]

#ans = numRollsToTarget(1, 6, 3)
ans = numRollsToTarget(30, 30, 500)
print(ans)