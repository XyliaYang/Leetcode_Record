# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 20:53
# @Author  : Xylia_Yang
# @Description ：

#
# 题目：矩阵中的路径
# 题：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
# 如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
#

"""
思路：回溯法，递归->
"""

def hasPath(matrix,str):
    """
    matrix中是否存在字符串str的路径
    :param matrix:
    :param str:
    :return:
    """
    if matrix is None or str is None:
        return False

    rows=len(matrix)
    cols=len(matrix[0])
    visited=[[False]*cols for i in range(rows)]

    pathLenth=0 # 遍历到str的第几个字符
    for row in range(rows):
        for col in range(cols):
            if hasPathCore(matrix,rows,cols,row,col,visited,str,pathLenth):
                return True

    return False

def hasPathCore(matrix,rows,cols,row,col,visited,str,pathLenth):
    """
    对matrix矩阵中第row行col列元素做判断，与str字符串中第pathLenth个字符串做判断
    :param matrix:
    :param row:
    :param col:
    :param visited:
    :param str:
    :param pathLenth:
    :return:
    """
    # 匹配成功
    if len(str) == pathLenth:
        return True

    ## 递归终止条件
    if row < 0 or row >= rows or col < 0 or col >= cols or str[pathLenth] != matrix[row][col] or visited[row][col]==True:
        return False


    visited[row][col]=True

    ## 上->下->左->右
    if hasPathCore(matrix,rows,cols,row-1,col,visited,str,pathLenth+1)or \
            hasPathCore(matrix, rows, cols, row +1, col, visited, str, pathLenth+1) or \
            hasPathCore(matrix, rows, cols, row , col-1, visited, str, pathLenth+1) or \
            hasPathCore(matrix, rows, cols, row , col+1, visited, str, pathLenth+1) :
        return True

    ## 该结点下一步没有路，当前访问情况。且回溯到第n-1个结点
    visited[row][col]=False
    return False

if __name__ =='__main__':
    matrix=[['a','b','t','g'],['c','f','c','s'],['j','d','e','h']]
    str='bfce'

    has_path=hasPath(matrix,str)
    # print(has_path)