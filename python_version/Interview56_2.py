# @Time : 2020/3/15 14:05
# @Author : Xylia_Yang
# @Description :

class Solution:
    def singleNumber(self, nums):
        if not nums:
            return

        numsOfbit=[0 for i in range(32)]

        for n in nums:
            temp=1

            for i in range(31,-1,-1):
                if n&temp:
                    numsOfbit[i]+=1
                temp=temp<<1

        result=0
        for i in range(32):
            result = result << 1
            result+=numsOfbit[i]%3

        return  result

if __name__=='__main__':
    solution=Solution()
    ls=[2,2,3,2]
    # print(solution.singleNumber(ls))
    print(bin(-4))
