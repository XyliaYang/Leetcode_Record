# @Time : 2020/3/31 12:00
# @Author : Xylia_Yang
# @Description :

class Solution:
    def wordBreak(self, s, wordDict) :
        if not s:
            return True
        if not wordDict:
            return False

        dp=[False]*(len(s)+1)

        dp[0]=True
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j]=True


        return dp[-1]
    
