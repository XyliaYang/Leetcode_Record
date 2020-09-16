# @Time : 2020/3/25 9:11
# @Author : Xylia_Yang
# @Description :


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root=TreeNode(preorder[0])
        left_size=0
        while inorder[left_size]!=root.val:
            left_size+=1

        if left_size>0:
            root.left=self.buildTree(preorder[1:left_size+1],inorder[:left_size])

        if preorder[left_size+1:]:
            root.right=self.buildTree(preorder[left_size+1:],inorder[left_size+1:])
        return root


if __name__=='__main__':
    preoder=[3,9,20,15,7]
    inorder=[9,3,15,20,7]
    solution=Solution()
    solution.buildTree(preoder,inorder)

