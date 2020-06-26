# idea:

# the way to the get to the last spot dp[m][n]


class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        if not n or not m:
            return 0

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[n - 1][m - 1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        for r in range(0, m):
            for c in range(0, n):
                if obstacleGrid[r][c] == 1:
                    continue
                if r == 0 and c == 0:
                    dp[r][c] = 1
                elif r == 0:
                    dp[r][c] = dp[r][c - 1]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c]
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]
