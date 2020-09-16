# @Time : 2020/2/23 17:53
# @Author : Xylia_Yang
# @Description :树的子结构，这里所考虑的情况和leetcode一致，子树的叶节点完全一致才完全一致.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        result=False
        if s and t:
            if s.val==t.val:
                result=self.isEqualtree(s,t)
            if not result:
                result=self.isSubtree(s.left,t)
            if not  result:
                result=self.isSubtree(s.right,t)
        return  result

    def isEqualtree(self,s,t):
        if not s and not t:
            return True
        if (s and not t) or (not s and t):
            return False
        if s.val !=t.val:
            return False
        return self.isEqualtree(s.left,t.left) and self.isEqualtree(s.right,t.right)



