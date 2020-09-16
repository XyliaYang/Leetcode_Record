# @Time : 2020/3/26 17:05
# @Author : Xylia_Yang
# @Description :

class Solution:
    def decodeString(self, s: str) -> str:
        if not str:
            return None

        tmp_stack=[]
        multi=0
        res=""

        for ch in s:
            if ch >='0' and ch<='9':

                multi=multi*10+int(ch)
            elif ch>='a' and ch<='z' or ch>='A' and ch<='Z':
                res+=ch
            elif ch=='[':
                tmp_stack.append([multi,res])
                multi=0
                res=""
            elif ch==']':
                [s_multi,s_res]=tmp_stack.pop()
                res=s_res+s_multi*res


        return  res
