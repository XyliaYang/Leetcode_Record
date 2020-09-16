# @Time : 2020/3/22 15:05
# @Author : Xylia_Yang
# @Description :

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return -1

        n=len(s)

        dp=[[False]*n for _ in range(n)]
        match_count=0

        for j  in range(n):
            col=j
            for i in range(n-j):
                if j==0:
                    dp[i][col]=True
                elif j==1:
                    dp[i][col]=(s[i]==s[col])
                else:
                    dp[i][col]=dp[i+1][col-1] and (s[i]==s[col])

                if dp[i][col]:
                    match_count+=1
                col+=1

        return match_count



if __name__=='__main__':
    solution=Solution()
    s="abc"
    print(solution.countSubstrings(s))
