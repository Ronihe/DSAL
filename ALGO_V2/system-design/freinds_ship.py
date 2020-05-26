class FriendshipService:

    def __init__(self):
        # initialize your data structure here.
        self.followers = dict()
        self.followings = dict()

    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def getFollowers(self, user_id):
        # Write your code here
        if user_id not in self.followers:
            return []
        results = list(self.followers[user_id])
        results.sort()
        return results

    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def getFollowings(self, user_id):
        # Write your code here
        if user_id not in self.followings:
            return []
        results = list(self.followings[user_id])
        results.sort()
        return results

    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id follows to_user_id
    def follow(self, to_user_id, from_user_id):
        # Write your code here
        if to_user_id not in self.followers:
            self.followers[to_user_id] = set()
        self.followers[to_user_id].add(from_user_id)

        if from_user_id not in self.followings:
            self.followings[from_user_id] = set()
        self.followings[from_user_id].add(to_user_id)

    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id unfollows to_user_id
    def unfollow(self, to_user_id, from_user_id):
        # Write your code here
        if to_user_id in self.followers:
            if from_user_id in self.followers[to_user_id]:
                self.followers[to_user_id].remove(from_user_id)

        if from_user_id in self.followings:
            if to_user_id in self.followings[from_user_id]:
                self.followings[from_user_id].remove(to_user_id)