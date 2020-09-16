# @Time : 2020/3/21 16:18
# @Author : Xylia_Yang
# @Description :

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t or len(s)<len(t):
            return ""

        res=""
        left=right=0
        res=s
        dict_t={}
        dict_window={}
        match_count=0  #用于判断目前window窗口有几组数值是满足t要求的

        for i in t:
            if i in dict_t.keys():
                dict_t[i]+=1
            else:
                dict_t[i]=1

        while right<len(s):
            item=s[right]
            if s[right] in dict_t.keys():
                dict_window[s[right]]=dict_window[s[right]]+1 if s[right] in dict_window.keys()  else 1

                if dict_window[s[right]] == dict_t[s[right]]: #尽在恰好==得时候加，避免后面有重复计数而多加
                    match_count += 1

            right+=1


            while match_count==len(dict_t):
                """
                若子串更小，则更新最终结果
                """
                if right-left<len(res):
                    res=s[left:right]

                if s[left] in dict_window.keys():
                    dict_window[s[left]]-=1

                    if dict_window[s[left]]<dict_t[s[left]]:
                        match_count-=1
                left+=1

        return  res


if __name__=='__main__':
    solution=Solution()
    s="ADOBECODEBANC"
    t="ABC"

    print(solution.minWindow(s,t))