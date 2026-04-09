import heapq

class Twitter:
    """
    
    user -> [(t1, tweet), (t2, tweet), (t3, tweet)]
    user -> set(following)

    """

    def __init__(self):
        self.user_to_tweets = defaultdict(list) 
        self.user_to_following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # k-way merge all user + follower tweets
        
        # add all initial ones to heap including own user
        # ((time, tweet), userId, index)

        # own user
        h = []
        heapq.heapify(h)
        if self.user_to_tweets[userId]: # checking that user has at least 1 tweet
            heapq.heappush(h, (
                self.user_to_tweets[userId][-1], userId, 
                len(self.user_to_tweets[userId])-1))

        # follower tweets
        for f in self.user_to_following[userId]:
            if f == userId: # edge case: users can follow themselves
                continue
            heapq.heappush(h, (
                self.user_to_tweets[f][-1], f,
                len(self.user_to_tweets[f])-1))
        
        res = []
        while h and len(res) != 10:
            (time, tweet), userId, i = heapq.heappop(h)
            res.append(tweet)

            # append next one, check that i-1 exists tho
            if i > 0:
                heapq.heappush(h, (
                    self.user_to_tweets[userId][i-1], userId,
                    i-1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_to_following[followerId].discard(followeeId)
