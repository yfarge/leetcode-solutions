# Recursive
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for j in range(n + 1)] for i in range(m + 1)]

        def dfs(i: int, j: int):
            if i >= m or j >= n:
                return 0

            if dp[i][j] is not None:
                return dp[i][j]

            if i == m - 1 and j == n - 1:
                return 1

            dp[i + 1][j] = dfs(i + 1, j)
            dp[i][j + 1] = dfs(i, j + 1)
            return dp[i + 1][j] + dp[i][j + 1]

        return dfs(0, 0)


# Iterative
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
