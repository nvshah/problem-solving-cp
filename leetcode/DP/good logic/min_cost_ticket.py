# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import List
from sys import maxsize

def mincostTickets(days: List[int], costs: List[int]) -> int:
    ''' O(38 * n) = (1 + 7 + 30) * n 
        => n for dfs() as each days is going to be visited once
           & 
           for each day in dfs we have to explore O(38) time
    '''
    dp = {} # cache to keep track of best cost at given day

    def getNextDay(idx, validDays):
        ''' Return index of Next day to Purchase Ticket
        '''
        currDay = days[idx]
        lastDay = currDay + validDays - 1   # last eligible day to use ticket of cost {c}
        for j in range(idx, len(days)):
            if days[j] > lastDay:
                break 
        else:
            j += 1  # all days are covered with this ticket

        return j

    def dfs(i):
        '''
        Find the cost from {day[i]} to last day travel
        i :- index of curr day being travelled
        '''
        if i == len(days):  # all days are travelled
            return 0

        if i in dp: 
            return dp[i]

        dp[i] = maxsize

        #expense = [c + dfs(getNextDay(i, d)) for d, c in zip([1,7,30], costs)] # expense of travelling journey with diff tickets from current day
        # dp[i] = min(expense)

        #Explore travelling with diff deal of ticket
        for d, c in zip([1,7,30], costs):
            # curr ticket purchased => {c} cost for {d} days
            # after travel d days at cost c, we need to buy ticket from next day {d+1}
            # so max days we can travel with the curr ticket purchased is d days
            
            # for j in range(i, len(days)):
            #     if days[j] > lastDay:
            #         break 
            # else:
            #     j += 1  # all days are covered with this ticket

            # Find the next day to buy ticket 
            #lastDay = days[i] + d - 1   # last eligible day to use ticket of cost {c}
            nextDay = days[i] + d
            
            j = i+1
            #while j < len(days) and days[j] <= lastDay:
            while j < len(days) and days[j] < nextDay:
                j += 1
                
            # (ie j -> index pointing to next day to but ticket)
            
            expense = c + dfs(j)
            dp[i] = min(dp[i], expense)

            #dp[i] = min(dp[i], c + dfs(j))

        return dp[i]

    return dfs(0)


def mincostTickets2(days: List[int], costs: List[int]) -> int:
    dp = {} # cache to keep track of best cost at given day

    def getNextDay(idx, validDays):
        ''' Return index of Next day to Purchase Ticket
        '''
        # currDay = days[idx]
        # lastDay = currDay + validDays - 1   # last eligible day to use ticket of cost {c}
        # for j in range(idx, len(days)):
        #     if days[j] > lastDay:
        #         break 
        # else:
        #     j += 1  # all days are covered with this ticket

        # return j
        j = idx+1
        lastDay = days[idx] + validDays - 1
        while j < len(days) and days[j] < lastDay:
            j += 1
        return j

    def dfs(i):
        '''
        Find the cost from {day[i]} to last day travel
        i :- index of curr day being travelled
        '''
        if i == len(days):  # all days are travelled
            return 0

        if i in dp: 
            return dp[i]

        dp[i] = maxsize

        expense = [c + dfs(getNextDay(i, d)) for d, c in zip([1,7,30], costs)] # expense of travelling journey with diff tickets from current day
        dp[i] = min(expense)

        return dp[i]

    return dfs(0)

    
            

