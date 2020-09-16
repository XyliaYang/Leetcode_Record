# @Time : 2020/2/27 21:53
# @Author : Xylia_Yang
# @Description :

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        right_index=0
        root=sequence[-1]
        leftisBST=True
        rightisBST=True

        # 找到左子树大于根节点的位置，作为左右左右子树的区分位置
        for i in  sequence[:-1]:
            if i>root:
                break
            right_index+=1

        # 若左子树有值，则继续判断是否为树。左子树为空则依然是true.
        if right_index:
            leftisBST=self.VerifySquenceOfBST(sequence[:right_index])

        # 若右子树有节点比根节点小，则直接返回false
        for i in sequence[right_index:-1]:
            if i<root:
                return False

        # 若右子树有大于1个以上的节点，则依然判断其是否为树，否则右子树是true.
        if len(sequence)-right_index-1:
            rightisBST=self.VerifySquenceOfBST(sequence[right_index:-1])


        return leftisBST and rightisBST



if __name__=='__main__':
    sequence=[4,8,6,12,16,14,10]
    solution=Solution()
    print(solution.VerifySquenceOfBST(sequence))
