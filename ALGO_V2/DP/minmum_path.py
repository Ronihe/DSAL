class Solution:
    """
    @param grid: a ist of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        n = len(grid)
        m = len(grid[0])

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        print(dp)

        return dp[n - 1][m - 1]


