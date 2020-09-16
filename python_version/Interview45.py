# @Time : 2020/2/29 9:38
# @Author : Xylia_Yang
# @Description :

from functools import cmp_to_key

class Solution:
    def PrintMinNumber(self, numbers):
        """
        sort的key指向一个item到key的映射，这个映射内容可以是自定义的一个排序方式,默认返回
        升序排列
        """
        numbers.sort(key=cmp_to_key(self.compare))
        res=''
        for i in numbers:
            res+=str(i)
        return res


    def compare(self,a,b):
        """
        这个自定义比较函数要满足一定要求：若传进来的第一个元素比第二个元素大，则return 1.
        小：return -1.等 ：return 0
        """
        str1=str(a)+str(b)
        str2=str(b)+str(a)

        if str1>str2:
            return 1
        elif str1<str2:
            return -1
        else:
            return 0

if __name__=='__main__':
    solution=Solution()
    sequence=[3,32,321]
    print(solution.PrintMinNumber(sequence))




