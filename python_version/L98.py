# @Time : 2020/3/29 11:49
# @Author : Xylia_Yang
# @Description :

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.pre=None


        def isBSTCore(root):
            left=right=True

            if  root.left:
                left=isBSTCore(root.left)

            if self.pre and self.pre.val>=root.val:
                return False
            self.pre=root

            if  root.right:
                right=isBSTCore(root.right)

            return left and right

        return isBSTCore(root)


if __name__=='__main__':
    solution=Solution()
    root=TreeNode(0)
    root.right=TreeNode(-1)


    print(solution.isValidBST(root))



