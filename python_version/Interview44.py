# @Time : 2020/3/10 19:58
# @Author : Xylia_Yang
# @Description :


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n<0:
            return

        digit=1
        while True:
            nums = self.countIntegers(digit)
            if n<nums*digit:
                return  self.natDigit(n,digit)

            n-=nums*digit
            digit+=1

    def countIntegers(self,digit):
        if digit==1:
            return 10

        return 9*pow(10,digit-1)


    def natDigit(self,n,digit):
        if digit==1:
            start_num=0
        else:
            start_num=pow(10,digit-1)

        index_num=int(n/digit)
        index_digit=n%digit

        num=start_num+index_num


        return  int(str(num)[index_digit])


if __name__=='__main__':
    n=20
    solution=Solution()
    print(solution.findNthDigit(n))




