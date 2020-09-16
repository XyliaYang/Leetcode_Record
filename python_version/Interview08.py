# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 9:21
# @Author  : Xylia_Yang
# @Description ：

# 题目：二叉树的下一个节点
# 题目描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


## 思路：1.有右子：找到右子树中最左的子结点 2.无右子是左子：父节点 3.无右子是右子：找到父节点是左子的父节点

class BinaryTreeNode:
    """
    带一个指向父节点的指针
    """
    def __init__(self,father=None,data=None):
        self.data=data
        self.fatherNode=father
        self.leftNode=None
        self.rightNode=None

def  ConstructBinaryTree(father,preOrder,inOrder):
    """
    构造包含父节点指向的二叉树
    :param father:
    :param preOrder:
    :param inOrder:
    :return:
    """
    rootNode = BinaryTreeNode(father=father)
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

    rootNode.leftNode=ConstructBinaryTree(rootNode,leftPreorder,leftInorder)
    rootNode.rightNode=ConstructBinaryTree(rootNode,rightPreorder,rightInorder)

    return rootNode

def  NextNode(pNode):
    """
    找出二叉树该结点的下一个结点
    :param pNode:
    :return:
    """
    if pNode is None:
        return None
    if pNode.rightNode is not  None:
        nextNode=pNode.rightNode
        while nextNode.leftNode is not None:
            nextNode=nextNode.leftNode

    elif pNode.fatherNode is not  None: # 无右子
        if pNode.fatherNode.leftNode is pNode: # 是左子
            nextNode=pNode.fatherNode
        else:   # 是右子
            nextNode=None
            curNode=pNode
            while curNode.fatherNode.fatherNode is not None:
                if curNode.fatherNode.fatherNode.leftNode is curNode.fatherNode:
                    nextNode=curNode.fatherNode.fatherNode
                    break
                curNode=curNode.fatherNode


    return nextNode


if __name__=='__main__':
    preOrder=['a','b','d','e','h','i','c','f','g']
    inOrder=['d','b','h','e','i','a','f','c','g']

    tree=ConstructBinaryTree(None,preOrder,inOrder)
    print(NextNode(tree.leftNode.rightNode.rightNode).data)

