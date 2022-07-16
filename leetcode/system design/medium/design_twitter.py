# https://leetcode.com/problems/design-twitter/

from collections import defaultdict, namedtuple
from heapq import heapify, heappop, heappush
from typing import List


class Twitter:

    def __init__(self):
        self.count = 0 # total numbers of tweet
        # users I'm following !
        self.followMap = defaultdict(set) # userId -> set of followeeId
        # total tweet by this user !
        self.tweetMap = defaultdict(list) # userId -> list of (count, tweetId)
        
        #self.MaxHeapItem = namedtuple('MaxHeapItem', ('itemId', 'userId', 'indexId', 'tweetId'))
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1
        
    def addUserTweetToMaxHeap(self, userId, tweetIdx, maxHeap):
        cntNum, tweetId = self.tweetMap[userId][tweetIdx]
        item = (-cntNum, tweetId, userId, tweetIdx)
        heappush(maxHeap, item)

    def getNewsFeed(self, userId: int) -> List[int]:
        
        # get all followee's (whom [userId follows])
        followees = self.followMap[userId]
        
        maxHeap = []
        res = []  # tweets as per recency
        
        # user + followees
        ids = [userId, *followees]
        
        # Get first k candidates
        for user in ids:
            # check if this user has tweeted any tweet
            if user in self.tweetMap:
                index = len(self.tweetMap[user]) - 1
                self.addUserTweetToMaxHeap(user, index, maxHeap)
        
        heapify(maxHeap)
        
        while maxHeap and len(res) < 10:
            _, tweetId, userId, index = heappop(maxHeap)
            res.append(tweetId)
            
            # add new tweet from same user
            if index > 0:
                nextIndex = index-1
                self.addUserTweetToMaxHeap(userId, nextIndex, maxHeap)
        
        return res
                

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)    


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,5)
print(obj.getNewsFeed(1))
obj.follow(1,2)
obj.postTweet(2,6)
print(obj.getNewsFeed(1))
obj.unfollow(1, 2)
print(obj.getNewsFeed(1))

