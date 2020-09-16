# @Time : 2020/2/26 15:31
# @Author : Xylia_Yang
# @Description :

class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        if not pushed and not popped:
            return True

        if not pushed or not popped:
            return False

        supplementary_stack=[]
        for pop_item in popped:
            while(supplementary_stack and supplementary_stack[-1]!=pop_item or not supplementary_stack):
                if pushed:
                    supplementary_stack.append(pushed[0])
                    pushed=pushed[1:]
                else:
                    return False
            supplementary_stack.pop()
        return True








