# @Time : 2020/3/3 14:04
# @Author : Xylia_Yang
# @Description :二叉搜索树与双向链表(返回双向链表的头节点)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None

        self.lastNode=None
        self.converCore(pRootOfTree)

        pHead=self.lastNode
        while pHead.left:
            pHead=pHead.left
        return pHead

    def converCore(self,pNode):
        if not pNode:
            return

        if pNode.left:
            self.converCore(pNode.left)

        pNode.left=self.lastNode

        if  self.lastNode:
            self.lastNode.right=pNode

        self.lastNode=pNode

        if pNode.right:
            self.converCore(pNode.right)
















