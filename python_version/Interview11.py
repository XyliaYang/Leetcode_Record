# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 18:13
# @Author  : Xylia_Yang
# @Description ：


# 题目： 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转（被移动的小数组中元素的位置不变）。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0

"""
思路：用p1指针指向数组第一个位置，p2指针指向最后一个元素位置。如果中间位置元素大于p1位置元素，就更新p1=mid;
如果中间位置元素小于p2位置，则p2=mid。知道p2p1相邻，p2指向元素即为所要查找的元素。
要考虑只移动0个元素的情况，以及01111变成10111或者11101这种情况必须按顺序查找。

"""
def MinRotateArr(rotateArr):
    """
    :param rotateArr:
    :return:
    """

    if len(rotateArr)==0 or  rotateArr is None:
        print('invalid input!')
        return
    p1=0
    p2=len(rotateArr)-1

    if rotateArr[p1]==rotateArr[p2]:
        return FindMinbyOrder(rotateArr) #顺序查找
    elif rotateArr[p1]<rotateArr[p2]: # 移动了前0个元素到末尾
        return rotateArr[p1]
    else:
        while p2-p1>1:
            mid=int((p2+p1)/2)
            if rotateArr[p1]<=rotateArr[mid]:
                p1=mid
            elif rotateArr[mid]<=rotateArr[p2]:
                p2=mid
        return rotateArr[p2]

def FindMinbyOrder(arr):
    min=arr[0]

    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]

    return min


if __name__=='__main__':
    rotateArr=[]
    print(MinRotateArr(rotateArr))
















