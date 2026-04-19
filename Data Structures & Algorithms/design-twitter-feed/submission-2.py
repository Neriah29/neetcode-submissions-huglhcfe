#let' try and break this down 
#intialise with following map, mapping each id to a set of following (including themself)
#posts array



class Twitter:

    def __init__(self):
        self.posts = deque([])
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #post, add to the posts array 
        self.posts.appendleft((tweetId, userId))

        # add the users to the following map
        self.following[userId].add(userId)


    def getNewsFeed(self, userId: int) -> List[int]:
        #we iterate over all the posts, 
        #select based on those in the users
        news = []
        for post in range(len(self.posts)):
            if post > 9:
                break
            if self.posts[post][1] in self.following[userId] or self.posts[post][1] == userId:
                news.append(self.posts[post][0])
        return news 
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # add them to the following map
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
