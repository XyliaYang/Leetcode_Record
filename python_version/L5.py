# @Time : 2020/4/5 16:26
# @Author : Xylia_Yang
# @Description :

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return None

        max_length=1
        max_res=s[0]

        n=len(s)

        dp=[[False]*n for _ in range(n)]

        for j in range(n):
            col=j
            for i in range(n-j):
                if j==0:
                    dp[i][col]=True
                elif j==1:
                    dp[i][col]=(s[i]==s[col])
                else:
                    dp[i][col]=dp[i+1][col-1] and (s[i]==s[col])

                if dp[i][col] and col-i+1>max_length:
                    max_length=col-i+1
                    max_res=s[i:col+1]

                col+=1

        return max_res

