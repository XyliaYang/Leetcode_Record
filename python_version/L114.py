# @Time : 2020/3/24 11:37
# @Author : Xylia_Yang
# @Description :

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while  root:
            if root.left:
                pre=root.left
                while pre.right:
                    pre=pre.right
                pre.right=root.right
                root.right=root.left
                root.left=None
            root=root.right



if __name__=='__main__':
    solution=Solution()
    node=TreeNode(1)
    node.left=TreeNode(2)
    node.right=TreeNode(5)
    node.left.left=TreeNode(3)
    node.left.right=TreeNode(4)
    node.right=TreeNode(5)
    node.right.right=TreeNode(6)
    solution.flatten(node)
