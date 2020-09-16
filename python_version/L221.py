# @Time : 2020/4/5 10:18
# @Author : Xylia_Yang
# @Description :

class Solution:
    def maximalSquare(self, matrix) :
        if not matrix:
            return 0

        rows=len(matrix)
        cols=len(matrix[0])

        dp=[[0]*(cols+1) for _ in range(rows+1)]

        max_length=0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='1':
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j],dp[i][j])+1

                    if dp[i+1][j+1]>max_length:
                        max_length=dp[i+1][j+1]

        return max_length**2