# https://leetcode.com/problems/smallest-string-with-swaps/
from collections import defaultdict

'''
Que
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
'''

'''
Idea :- Union & Find | defaultdict | 
'''

def smallestStringWithSwaps(s, pairs):
    """
    :type s: str
    :type pairs: List[List[int]]
    :rtype: str
    """
    l = len(s)
    # initially all characters are parent to themselves
    parents = [i for i in range(l)]  

    # Here rank will be ordinal val of character (ie ord(char))
    ranks = [1] * l

    def find(v):
        '''find the parent for this member {v} in the graph'''
        p = v   # every elem {v} has atleast parent itself in worst case

        # 1. find the root
        while p != parents[p]:
            p = parents[p]

        # 2. Path Compression for all members of P's grp
        while v != p: 
            parents[v], v = p, parents[v]

        # {p} is the root of group where {v} belongs
        return p

    def union(v1, v2):
        ''' Find or Form a Group S.t the lexiographically small candidate become parent or root '''
        # root parents for both the elem {v1} & {v2}
        p1, p2 = find(v1), find(v2) 

        if p1 == p2:  # both of them already belong to same group
            return

        # new group need to be formed
        if p1 <= p2:
            # {p1} is lexiographicallly small than {p2}
            parents[p2] = p1
            ranks[p2] = 0
        else:
            # {p2} is lexiographicallly small than {p1}
            parents[p1] = p2
            ranks[p1] = 0

    # Find parents
    for p in pairs:
        union(*p)

    # Compress 1 last time (to deal with residual ranks)
    for i in range(l):
        p = parents[i]
        if not ranks[p]:
            parents[i] = parents[p]

    #print(parents)

    # create grps
    grp = defaultdict(list)
    for i in range(l):
        grp[parents[i]].append(i)

    #print(grp)

    # sort each grp
    for k in grp:
        grp[k].sort(reverse=True, key=s.__getitem__)

    ans = ['']*l
    # create ans
    for i in range(l):
        ans[i] = s[grp[parents[i]].pop()]

    return ''.join(ans)
            