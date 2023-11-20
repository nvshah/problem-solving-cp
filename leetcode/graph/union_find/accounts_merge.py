# https://leetcode.com/problems/accounts-merge/solutions/

from bisect import insort
from collections import defaultdict
from itertools import count, groupby, chain
from typing import List
from functools import cmp_to_key

'''
Union Find (Disjoint Set Union)
'''


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)] # parent of each group
        self.grpCnt = n  # total groups
    
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        pre_x = self.find(x)
        pre_y = self.find(y)
        if pre_x != pre_y: # if not merged already 
            # Surely the first [x] would be the lead of group based on first come first serve
            self.parent[pre_y] = pre_x 
            self.grpCnt -= 1

class Solution:
    def accountsMerge(self, accounts:  List[List[str]]) -> List[List[str]]:
        emailToAcc = {}  # email -> account_idx
        uf = UnionFind(len(accounts))

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    # Already account registered in some group
                    rootGrpId = emailToAcc[email]
                    uf.union(rootGrpId, idx)   # club current account to registered group
                else:
                    # Account not registered yet
                    emailToAcc[email] = idx
        
        # Now the Accounts info is clubbed

        emailGroup = defaultdict(list) # account's idx -> [emails]
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name, *sorted(emails)])

        return res

class Solution2:
    def accountsMerge(self, accounts:  List[List[str]]) -> List[List[str]]:
        emailToAcc = {}  # email -> account_idx
        uf = UnionFind(len(accounts))

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    # Already account registered in some group
                    rootGrpId = emailToAcc[email]
                    uf.union(rootGrpId, idx)   # club current account to registered group
                else:
                    # Account not registered yet
                    emailToAcc[email] = idx
        
        # Now the Accounts info is clubbed

        # counter mechanism to find the pos of unique grp in result list
        cntr = count()
        grpToPos = defaultdict(cntr.__next__)
        merged = [[] for _ in range(uf.grpCnt)]

        # Combine all emails to specific group
        for email, accId in emailToAcc.items():
            grpId = uf.find(accId)  # this [accId] belongs to which grp ?
            pos = grpToPos[grpId]
            insort(merged[pos], email)  # Insertion Sort to maintain order

        # Add name at the start of each merged result
        for accId, mergePos in grpToPos.items():
            name = accounts[accId][0]
            merged[mergePos].insert(0, name)

        return merged


class Solution3:
    
    '''NOT WORKING'''

    def accountsMerge(self, accounts:  List[List[str]]) -> List[List[str]]:
        def getKey(a, b):
            if a[1] & b[1]:
                return 0
            return -1

        re_accounts = map(lambda x: [x[0], set(x[1:])], accounts)
        group = groupby(re_accounts, key=cmp_to_key(getKey))
        merged = []
        included = defaultdict(list) # name -> []
        for _, v in group:
            grp = list(v)  # v := [[name, {mails}], [name, {mails}]]
            print(grp)
            name = grp[0][0]
            emails = set().union(*map(lambda x: x[1], grp))
            
            basket = included[name]
            if basket and any(filter(lambda mails: emails == mails, basket)):
                continue
        
            sEmails = sorted(emails)
            merged.append([name, *sorted(emails)])
            included[name].append(emails)
        
        print(included)
        
        return merged

accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
a = Solution2()
ans = a.accountsMerge(accounts)
print(ans)
        