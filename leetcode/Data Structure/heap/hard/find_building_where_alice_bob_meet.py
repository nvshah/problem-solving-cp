from collections import defaultdict
from operator import itemgetter
from typing import List
from itertools import groupby
import heapq

"""
Idea we will achieve this via maintaining heap of query we see till now
so that
we can avoid multiple linear search
ie
We will check it reverse way (given each index -> which queries solutions it can possibly be)
"""


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        # 1. group the queries by end-index
        # ? We need to find what all queries end at particular index so that we can answer them as we proceed in linear scan
        # ? Why end position because end comes after start so once we see end we can say that we have seen/accounted entire query

        ans = [-1] * len(queries)

        # queries that fall for given end position
        # endpos -> (max_val_in_query, query_number)
        end_pos_to_queries_map = defaultdict(list)
        for i, (a, b) in enumerate(queries):
            if a == b:
                # we know the ans upfront
                ans[i] = a
                continue  # no need to track this query for possible solution

            # end = max(a, b, key = lambda x: heights[x])
            s, e = sorted((a, b))
            if heights[s] < heights[e]:
                ans[i] = e
                continue

            max_height = max(heights[s], heights[e])
            end_pos_to_queries_map[e].append((max_height, i))

        # ? why used heapq - so that always given candidate we may not need to do full linear scan for potential elgiible queries

        # min heap - track queries as per their max-height demand (ensuring all queries get attained efficiently)
        # we will feed this from above computed map asa we reach end-index
        # we will find all possible queries avalable for that end-index and will push into this heap so that
        # moving onwards we can find the correct ans position
        minheap = []

        # 2. Linear scan for possible answers
        # explore given height, which query ans it can be
        for i, height in enumerate(heights):
            if queries := end_pos_to_queries_map.get(i, None):
                for query_info in queries:
                    heapq.heappush(minheap, query_info)

            while minheap and height > minheap[0][0]:
                # [height] is an ans to next query in our heap !
                _, query_idx = heapq.heappop(minheap)
                # height found at position i hence assigning position
                ans[query_idx] = i

        return ans
