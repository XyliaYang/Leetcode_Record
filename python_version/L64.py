# @Time : 2020/3/22 11:22
# @Author : Xylia_Yang
# @Description :

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid:
            return -1

        rows=len(grid)
        cols=len(grid[0])

        dp=[[None]*cols for _ in range(rows)]


        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif i==0:
                    dp[i][j]=dp[i][j-1]+grid[i][j]
                elif j==0:
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]

        return dp[-1][-1]


