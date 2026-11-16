class Twitter:

    def __init__(self):
        self.following = collections.defaultdict(set) # userId: followingSet
        self.tweets = collections.defaultdict(list) # userId: tweetsList (time, tweetId)
        self.time = 1 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        curr_following = self.following[userId]
        
        for person in curr_following | set([userId]):
            feed = self.tweets[person]
            if feed: 
                index = len(feed) - 1
                tweet = self.tweets[person][index]
                t = tweet[0]
                heapq.heappush(heap, (-t, person, index))
        
        while heap and len(res) < 10:
            _, person, index = heapq.heappop(heap)
            res.append(self.tweets[person][index][1])

            if index > 0:
                new_index = index - 1
                tweet = self.tweets[person][new_index]
                t = tweet[0]
                heapq.heappush(heap, (-t, person, new_index))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

