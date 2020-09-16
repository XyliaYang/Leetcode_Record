# @Time : 2020/3/22 10:31
# @Author : Xylia_Yang
# @Description :

class Solution:
    def numTrees(self, n: int) -> int:
        if n<1:
            return 0
        dp=[0]*(n+1)

        dp[0]=1
        dp[1]=1

        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]

        return dp[-1]



if __name__=='__main__':
    solution=Solution()
    print(solution.numTrees(3))