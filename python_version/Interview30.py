# @Time : 2020/2/26 13:54
# @Author : Xylia_Yang
# @Description :

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_stack=[]
        self.min_stack=[]

    def push(self, x: int) -> None:
        self.data_stack.append(x)
        if len(self.min_stack):
            min=self.min_stack[-1]
            if x<min:
                self.min_stack.append(x)
            else:
                self.min_stack.append(min)
        else:
            self.min_stack.append(x)


    def pop(self) -> None:
        self.min_stack.pop()
        return  self.data_stack.pop()

    def top(self) -> int:
        return  self.data_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

