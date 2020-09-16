# @Time : 2020/3/22 16:01
# @Author : Xylia_Yang
# @Description :

class Solution:
    def numSquares(self, n: int) -> int:
        if n<1:
            return 0

        r = int(n**0.5)
        if r * r == n:
            return  1

        dp=[i for i in range(n+1)]

        for i in range(1,n+1):
            r = int(i**0.5)
            if r * r == i:
                dp[i]=1
            else:
                for j in range(1,int(i**0.5)+1):
                    dp[i]=min(dp[i],dp[i-j*j]+1)


        return dp[n]



if __name__=='__main__':
    solution=Solution()
    print(solution.numSquares(12))






