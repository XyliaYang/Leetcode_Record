# @Time : 2020/3/16 20:54
# @Author : Xylia_Yang
# @Description :

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return

        str_arr=s.split(' ')
        str_arr.reverse()

        return ' '.join(str_arr)


