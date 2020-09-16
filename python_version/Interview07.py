# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 20:19
# @Author  : Xylia_Yang
# @Description ：

# 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

## 思路：由递归的方式。先由前序遍历第一个数得到根的数，再由根的数放入到中序遍历中划分出左子树和右子树的序列，
## 递归构建左子树和右子树

class BinaryTreeNode:
    def __init__(self,data=None):
        self.data=data
        self.leftNode=None
        self.rightNode=None

def  ConstructBinaryTree(preOrder,inOrder):
    rootNode = BinaryTreeNode()
    if len(preOrder)==0: # 序列里没有数
        return rootNode

    rootNode.data = preOrder[0]
    if preOrder[0]==preOrder[-1]: # 序列里只有一个数
        if inOrder[0]==inOrder[-1]:
            return rootNode
        else:
            print('error order!\n')

    ## 在中序遍历中找到根节点的位置
    for i in range(len(inOrder)):
        if inOrder[i]==preOrder[0]:
            leftPreorder=preOrder[1:1+i]
            rightPreorder=preOrder[1+i:]
            leftInorder=inOrder[:i]
            rightInorder=inOrder[i+1:]
            break

    rootNode.leftNode=ConstructBinaryTree(leftPreorder,leftInorder)
    rootNode.rightNode=ConstructBinaryTree(rightPreorder,rightInorder)

    return rootNode


if __name__=='__main__':
    preOrder=[1,2,4,7,3,5,6,8]
    inOrder=[4,7,2,1,5,3,8,6]

    tree=ConstructBinaryTree(preOrder,inOrder)
    print(tree.data)

















