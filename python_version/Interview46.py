# @Time : 2020/2/29 14:53
# @Author : Xylia_Yang
# @Description :

class Solution:
    def numDecodings(self, s: str) -> int:
        if not str:
            return 0
        return self.haveDecodingsfromIndex(s,0)

    def haveDecodingsfromIndex(self,str,index):
        if index==len(str)-1:
            return 1
        if index==len(str)-2:
            num=int(str[index:index+2])
            if num>26:
                return 1
            if num<=26 and num>=1:
                return 2

        return self.haveDecodingsfromIndex(str,index+1)+self.from10to26(str,index)*self.haveDecodingsfromIndex(str,index+2)

    def from10to26(self,str,index):
        num=int(str[index:index+2])
        if num>=10 and num<=26:
            return 1
        else:
            return 0




if __name__=='__main__':
    solution=Solution()
    print(solution.numDecodings("0"))
    a="0"
    print(a=="0")