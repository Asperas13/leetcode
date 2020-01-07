from collections import defaultdict
from heapq import heappush, heappushpop, nlargest


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_to_tweets = defaultdict(list)
        self.user_to_followees = defaultdict(set)
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.user_to_tweets[userId].append((self.order, tweetId))
        self.order += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feed = []
        followees = self.user_to_followees[userId]
        if userId not in followees:
            followees.add(userId)

        for folowee in followees:
            last_10_tweets = self.user_to_tweets[folowee][-10:]
            for tweet in last_10_tweets:
                if len(feed) < 10:
                    heappush(feed, tweet)
                else:
                    heappushpop(feed, tweet)

        return [tweet_id[1] for tweet_id in nlargest(10, feed)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_to_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.user_to_followees[followerId]:
            self.user_to_followees[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)