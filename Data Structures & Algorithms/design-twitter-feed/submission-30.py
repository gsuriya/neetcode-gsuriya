class Twitter:
    """

    post
    unfollow/follow

    user --> u1, u2, u3, u4, u5
     |       |    |  |    |  |
    ts      ts    ts ts   ts ts

    from all the ts, most recent tweets r at the end

    k-way list merge to find 10 largest times at the end

    [1, 2, 6]
    [4, 5, 10]
    [3, 11]

    1. add all endings to maxh
      (-time, tweet_id, user_id, index)
    2. while res < 10
    - pop from maxheap, put corresponding tweet_id in res
    - push next element into maxheap using popped index

    """
    def __init__(self):
        self.time = 0 # used to compare tweet timings between each user
        self.user_to_follows = defaultdict(set) # user --> set(ppl they follow)
        self.user_posts = defaultdict(list) # user --> [(time, tweet_id)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # set of all users with tweet_lists we gotta merge
        all_users = {userId} | self.user_to_follows[userId]
        maxh = []
        heapq.heapify(maxh)

        # add last element in each tweet list to maxheap
        for u in all_users:
            if self.user_posts[u]:
                time, tweet_id = self.user_posts[u][-1]
                i = len(self.user_posts[u])-1
                heapq.heappush(maxh, (-time, tweet_id, u, i))

        res = []
        while maxh and len(res) < 10:
            t, tweet_id, u, i = heapq.heappop(maxh)
            res.append(tweet_id)

            # find next element to push into maxheap if it exists
            if i > 0:
                time, tweet_id = self.user_posts[u][i-1]
                heapq.heappush(maxh, (-time, tweet_id, u, i-1))

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_to_follows[followerId].discard(followeeId)

        
