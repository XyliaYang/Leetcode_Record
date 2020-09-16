# -*- coding: utf-8 -*-
# @Time    : 2019/11/17 17:16
# @Author  : Xylia_Yang
# @Description ：
#
# // 面试题4：二维数组中的查找
#     // 题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
#     // 照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
#     // 整数，判断数组中是否含有该整数。

## 思路：从矩阵右上方元素开始比较，查找数字小于他，则舍弃改元素所在列；
# 若查找数据大于他，则舍弃该元素舍弃行。

def find(matrix,number):
    """
    :param matrix: 所查找的数组
    :param number:所查找的数字
    :return:
    """

    if matrix is not None:
        rows = len(matrix)
        colums = len(matrix[0])
        row=0
        colum=colums-1

        while row<rows and colum>0:
            if matrix[row][colum]==number:
                return True
            elif matrix[row][colum]>number:
                colum-=1
            else:
                row+=1

    return False


if __name__=='__main__':
    arr=None
    number=20

    print(find(arr,number))




