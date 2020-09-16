# @Time : 2020/3/9 20:50
# @Author : Xylia_Yang
# @Description :

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not str:
            return

        char_index=[]
        for i in range(26):
            char_index.append(-1)

        pre_max=0
        str_max=0
        for i in range(len(s)):
            if char_index[ord(s[i])-ord('a')]==-1:
                cur_max=pre_max+1
            elif  i-char_index[ord(s[i])-ord('a')]<=pre_max:
                cur_max=i-char_index[ord(s[i])-ord('a')]
            else:
                cur_max=pre_max+1
            char_index[ord(s[i])-ord('a')] = i
            pre_max=cur_max

            if cur_max>str_max:
                str_max=cur_max
        return str_max


if __name__=='__main__':
    str="arabcacfr"
    solution=Solution()
    print(solution.lengthOfLongestSubstring(str))



