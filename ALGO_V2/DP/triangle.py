# https://www.lintcode.com/problem/triangle/description

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]

# Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# solutions:
# 1. DFS: traverse
# 2. divide and conquer
# 3. divide and conquer + memorization
# 4. traditional dp

# dfs
import sys


class Solution_dfs:
    """
    time complexity: O(2**n)

    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        self.minimum = sys.maxsize
        self.dfs(triangle, 0, 0, 0)
        return self.minimum

        # write your code here

    def dfs(self, triangle, x, y, path_sum):
        if x == len(triangle):
            self.minimum = min(self.minimum, path_sum)
            return

        self.dfs(triangle, x + 1, y, path_sum + triangle[x][y])
        self.dfs(triangle, x + 1, y + 1, path_sum + triangle[x][y])


# divide conquer
class Solution_divide_conquer:
    """
     time complexity: O(2**n)

    """

    def minimumTotal(self, triangle):
        return self.divde_conquer(triangle, 0, 0)

    def divde_conquer(self, triangle, x, y):
        if x == len(triangle):
            return 0

        left = self.divde_conquer(triangle, x + 1, y)
        right = self.divde_conquer(triangle, x + 1, y + 1)

        return min(left, right) + triangle[x][y]


# memorization:
# no dup calculation
# memorization is a type of dp

class Solution_memorization:
    """
     bottom up, the top if the min of the left down and right down
     time: O(n ** 2)
     space: O(n ** 2)

    """

    def minimum_total(self, triangle):
        return self.divide_conquer(triangle, 0, 0, {})

    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0

        if (x, y) in memo:
            return memo[(x, y)]
        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y, memo)

        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]

    def minimum_total_bottomup(self, triangle):
        n = len(triangle)
        #         state : dp[i][j] mean the shortest way to get to the bottom

        dp = [[0] * (i + 1) for i in range(n)]

        #         init the bottom row
        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]
        #  from bottom up to see where should it go
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        # answer is the top of the dp
        return dp[0][0]

    def minimum_total_top_down(self, triangle):
        n = len(triangle)
        # state: dp[i][j] means shortest way tp go to the spot
        dp = [[0] * (i + 1) for i in range(n)]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        # answer: the last row, any position can be the end of a route
        return min(dp[n - 1])
