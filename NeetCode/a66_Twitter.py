from typing import List
from collections import deque
from collections import defaultdict
import heapq

# 2. Heap
class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        print(f"***postTweet userId: {userId}, tweetId: {tweetId}")
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        print(f"userId: {userId}, count: {self.count}")

    def getNewsFeed(self, userId: int) -> List[int]:
        print(f"***getNewsFeed userId: {userId}")
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                print(f"userId: {userId}, count: {count}, followeeId: {followeeId} tweetId: {tweetId}")
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        print(f"***follow followerId: {followerId}, followeeId: {followeeId}")
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print(f"***unfollow followerId: {followerId}, followeeId: {followeeId}")
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Time complexity: O(n) for each getNewsFeed() call and O(1) for remaining methods.
# Space complexity: O(N∗m+N∗M+n)


#below returns false because of the order of the tweets
class Twitter2:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets.keys():
            d = deque([])
            self.tweets[userId] = d
        self.tweets[userId].append(tweetId)
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()   

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        people = []
        people.append(userId)
        if userId in self.following:
            for followee in self.following[userId]:
                people.append(followee)
        for userId in people:
            for tw in self.tweets[userId]:
                ans.append(tw)
        # ans.sort()        
        return ans                
            
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        if followerId not in self.following.keys():
            self.following[followerId] = []
        self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        self.following[followerId].remove(followeeId)

twitter = Twitter()
print(twitter.postTweet(1, 10))  # User 1 posts a new tweet with id = 10.
print(twitter.postTweet(2, 20))  # User 2 posts a new tweet with id = 20.
print(twitter.postTweet(3, 30))  
print(twitter.postTweet(1, 40))  
print(twitter.getNewsFeed(1))    # User 1's news feed should only contain their own tweets -> [10].
print(twitter.getNewsFeed(2))    # User 2's news feed should only contain their own tweets -> [20].
print(twitter.follow(1, 2))      # User 1 follows user 2.
print(twitter.getNewsFeed(1))    # User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
print(twitter.getNewsFeed(2))    # User 2's news feed should still only contain their own tweets -> [20].
print(twitter.unfollow(1, 2))    # User 1 unfollows user 2.
print(twitter.getNewsFeed(1))    # User 1's news feed should only contain their own tweets -> [10].


# Design Twitter
# Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

# Users and tweets are uniquely identified by their IDs (integers).

# Implement the following methods:

# Twitter() Initializes the twitter object.
# void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
# List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.
# Example 1:

# Input:
# ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]

# Output:
# [null, null, null, [10], [20], null, [20, 10], [20], null, [10]]

# Explanation:
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
# twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
# twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
# twitter.follow(1, 2);     // User 1 follows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
# twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
# twitter.unfollow(1, 2);   // User 1 follows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
# Constraints:

# 1 <= userId, followerId, followeeId <= 100
# 0 <= tweetId <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time for each getNewsFeed() function call, O(1) time for the remaining methods, and O((N * m) + (N * M) + n) space, where n is the number of followeeIds associated with the userId, m is the maximum number of tweets by any user, N is the total number of userIds, and M is the maximum number of followees for any user.


# Hint 1
# Can you think of a data structure to store all the information, such as userIds and corresponding followeeIds, or userIds and their tweets? Maybe you should think of a hash data structure in terms of key-value pairs. Also, can you think of a way to determine that a tweet was posted before another tweet?


# Hint 2
# We use a hash map followMap to store userIds and their unique followeeIds as a hash set. Another hash map, tweetMap, stores userIds and their tweets as a list of (count, tweetId) pairs. A counter count, incremented with each tweet, tracks the order of tweets. The variable count is helpful in distinguishing the time of tweets from two users. This way of storing data makes the functions follow(), unfollow(), and postTweet() run in O(1). Can you think of a way to implement getNewsFeed()? Maybe consider a brute force approach and try to optimize it.


# Hint 3
# A naive solution would involve taking the tweets of the userId and its followeeIds into a list, sorting them in descending order based on their count values, and returning the top 10 tweets as the most recent ones. Can you think of a more efficient approach that avoids collecting all tweets and sorting? Perhaps consider a data structure and leverage the fact that each user's individual tweets list is already sorted.


# Hint 4
# We can use a Max-Heap to efficiently retrieve the top 10 most recent tweets. For each followee and the userId, we insert their most recent tweet from the tweetMap into the heap, along with the tweet's count and its index in the tweet list. This index is necessary because after processing a tweet, we can insert the next most recent tweet from the same user's list. By always pushing and popping tweets from the heap, we ensure that the 10 most recent tweets are retrieved without sorting all tweets.