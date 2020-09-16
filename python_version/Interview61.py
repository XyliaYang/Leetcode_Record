# @Time : 2020/3/17 10:05
# @Author : Xylia_Yang
# @Description :

# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers or len(numbers)<5:
            return False

        numbers.sort()
        numofZero=0
        gapofZero=0

        for i in numbers:
            if i==0:
                numofZero+=1
            if i!=0:
                break

        small_index=numofZero
        big_index=small_index+1

        while big_index<len(numbers):
            if numbers[small_index]==numbers[big_index]:
                return False

            gapofZero+=(numbers[big_index]-numbers[small_index]-1)
            if gapofZero>numofZero:
                return False

            small_index+=1
            big_index+=1

        return True


if __name__=='__main__':
    solution=Solution()
    nums=[1,3,2,5,4]

    print(solution.IsContinuous(nums))
