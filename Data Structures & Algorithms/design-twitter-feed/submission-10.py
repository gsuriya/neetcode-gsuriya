import heapq

class Twitter:

    def __init__(self):
        self.user_to_tweets = defaultdict(list)  # user -> [(time, tweetId)]
        self.user_to_follows = defaultdict(set) # user -> set(followees)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []

        # include self + followees
        users = self.user_to_follows[userId] | {userId}

        # push MOST RECENT tweet per user
        for user in users:
            tweets = self.user_to_tweets[user]
            if tweets:
                time, tweet_id = tweets[-1]
                heapq.heappush(h, (-time, tweet_id, len(tweets) - 1, user))

        res = []
        while h and len(res) < 10:
            neg_time, tweet_id, i, user = heapq.heappop(h)
            res.append(tweet_id)

            # push next older tweet from same user
            if i > 0:
                time, tweet_id = self.user_to_tweets[user][i - 1]
                heapq.heappush(h, (-time, tweet_id, i - 1, user))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_to_follows[followerId]:
            self.user_to_follows[followerId].remove(followeeId)