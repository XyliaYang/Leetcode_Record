# @Time : 2020/3/22 9:42
# @Author : Xylia_Yang
# @Description :

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if  n<1:
            return 0

        dp=[[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]