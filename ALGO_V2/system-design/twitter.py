# https://www.lintcode.com/problem/design-twitter/description

# postTweet(user_id, tweet_text). Post a tweet.
# getTimeline(user_id). Get the given user's most recently 10 tweets posted by himself, order by timestamp from most recent to least recent.
# getNewsFeed(user_id). Get the given user's most recently 10 tweets in his news feed (posted by his friends and himself). Order by timestamp from most recent to least recent.
# follow(from_user_id, to_user_id). from_user_id followed to_user_id.
# unfollow(from_user_id, to_user_id). from_user_id unfollowed to to_user_id.

class Tweet:
    tweet = []

    @classmethod
    def create(cls, user_id, tweet_text):
        cls.tweet.append((user_id, tweet_text))

    def __init__(self, num):
        self.tweet = num


test = Tweet.create(1, "hi")
print(Tweet.tweet)
print(Tweet.tweet)

t1 = Tweet(41)
t2 = Tweet(43)
print(t1.tweet, t1.__class__.tweet)
print(t2.tweet, t2.__class__.tweet)


class MiniTwitter:

    def __init__(self):
        self.order = 0
        self.users_tweet = {}
        self.friends = {}

    def postTweet(self, user_id, tweet_test):
        tweet = Tweet.create(user_id, tweet_test)
        self.order += 1
        if user_id in self.users_tweet:
            self.users_tweet[user_id].append((self.order, tweet))
        else:
            self.users_tweet[user_id] = [(self.order, tweet)]

    def getNewsFeed(self, user_id):
        rt = []
        if user_id in self.friends:
            for friend in self.friends[user_id]:
                if friend in self.users_tweet:
                    rt.extend(self.users_tweet[friend][-10:])

        rt.sort(key=lambda x: x[0])
        return [t[1] for t in rt[-10:][::-1]]

    def getTimeLine


    def follow(self, from_uder):