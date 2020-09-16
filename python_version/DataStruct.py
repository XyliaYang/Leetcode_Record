# @Time : 2020/2/28 18:48
# @Author : Xylia_Yang
# @Description : 这里面有一些基本数据结构的方法，方便初始化


# 1.单行输入
n=int(input())

# 2.单行以空格输入数组
str_in = input()
a = [int(n) for n in str_in.split(' ')]

# 3.输出
print("%.2f"%sum)

# 4.空格间隔输出
x=[]
print(' '.join(str(i) for i in x))


"""
二叉树节点
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None






