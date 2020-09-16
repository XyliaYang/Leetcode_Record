# @Time : 2020/3/12 8:37
# @Author : Xylia_Yang
# @Description :

class Solution_1:
    def nthUglyNumber(self, n: int) -> int:
        if n<=0:
            return

        num=0
        count=0
        while count<n:
            num+=1
            if self.isUgly(num):
                count+=1

        return num

    def isUgly(self,num):
        while num%2==0:
            num/=2
        while num%3==0:
            num/=3
        while num%5==0:
            num/=5
        return  num==1



## 思路二
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n<=0:
            return
        p=[1]
        index_2=index_3=index_5=0

        for _ in range(n-1):
            next_data = min(p[index_2] * 2, p[index_3] * 3, p[index_5] * 5)
            p.append(next_data)

            if next_data == p[index_2] * 2:
                index_2 += 1
            if next_data == p[index_3] * 3:
                index_3 += 1
            if next_data == p[index_5] * 5:
                index_5 += 1

        return p[-1]


