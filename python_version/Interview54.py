# @Time : 2020/3/13 17:53
# @Author : Xylia_Yang
# @Description :


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthNode(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: TreeNode
        """
        if not root:
            return

        self.arr=[]
        self.countKthNode(root)

        if k<len(self.arr):
            return self.arr[k - 1].val
        else:
            return -1

    def countKthNode(self,root):

        if root.left:
            self.countKthNode(root.left)

        self.arr.append(root)

        if root.right:
            self.countKthNode(root.right)




if __name__=='__main__':
    root=TreeNode(5)
    root.left=TreeNode(3)
    root.left.left=TreeNode(2)
    root.left.right=TreeNode(4)
    root.right=TreeNode(7)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(8)

    solution=Solution()
    print(solution.kthNode(root,3))

