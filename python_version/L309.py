# @Time : 2020/3/31 10:50
# @Author : Xylia_Yang
# @Description :

class Solution:
    def maxProfit(self, prices) :
        if not prices or len(prices)<2:
            return 0


        dp=[[0]*3 for _ in range(len(prices))]

        dp[0][0]=0
        dp[0][1]=-prices[0]
        dp[0][2]=0

        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][2]-prices[i],dp[i-1][1])
            dp[i][2]=dp[i-1][0]

        return max(dp[len(prices)-1][0],dp[len(prices)-1][2])