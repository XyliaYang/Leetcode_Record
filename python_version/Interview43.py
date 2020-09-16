# @Time : 2020/3/9 17:57
# @Author : Xylia_Yang
# @Description :

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n<1:
            return

        count=0
        for num in range(1,n+1):
            temp=num

            while temp:
                if temp%10==1:
                    count+=1
                temp=int(temp/10)
        return  count


if __name__=='__main__':
    num=13
    solution=Solution()
    print(solution.countDigitOne(num))

