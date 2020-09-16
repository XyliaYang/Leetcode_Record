# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 14:58
# @Author  : Xylia_Yang
# @Description ：

# 题目：用两个栈实现队列
# 题目描述：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# 思路：入队列：直接压栈到stack1；
# 出队列：如果stack2不空，则从stack2中出栈；
# 若stack2为空，则从stack1出栈的元素全部压栈到Stack2中，再从stack2中出栈
class QueuebyStack:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]

    def  appendTail(self,data):
        self.stackA.append(data)

    def  deleteHead(self):
        if len(self.stackB)>0: # stackB非空
            return self.stackB.pop()
        else: # stackB空
            if len(self.stackA)==0:
                print('queue is empty!')
            else:
                while len(self.stackA) > 0:
                    self.stackB.append(self.stackA.pop())
                return self.stackB.pop()
    def isEmpty(self):
        return self.stackA==[] and self.stackB==[]


# 题目拓展：用两个队列实现栈
## 思路：入栈：入不空的queue,否则入任意空的queue;
# 出栈：从非空的queue1出队列到入队列到另一个队列，出queue1的最后一个元素
class Queue:
    """
    python 没有直接的queue接口,用list实现
    """
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]
    def enQueue(self,item):
        self.items.insert(0,item)
    def deQueue(self):
        return self.items.pop()
    def sizeQueue(self):
        return len(self.items)

class StackbyQueue:
    def __init__(self):
        self.queueA=Queue()
        self.queueB=Queue()

    def enQueue(self,item):
        if  not self.queueA.isEmpty():
            self.queueA.enQueue(item)
        elif not self.queueB.isEmpty():
            self.queueB.enQueue(item)
        else:
            self.queueA.enQueue(item)

    def deQueue(self):
        if not self.queueA.isEmpty():
            while self.queueA.sizeQueue()>1:
                self.queueB.enQueue(self.queueA.deQueue())
            return self.queueA.deQueue()

        elif not self.queueB.isEmpty():
            while self.queueB.sizeQueue()>1:
                self.queueA.enQueue(self.queueB.deQueue())
            return self.queueB.deQueue()
        else:
            print('stack is empty!')

    def isEmpty(self):
        return  self.queueA.isEmpty() and self.queueB.isEmpty()


if __name__=='__main__':
    print('queue by stack:\n')
    q=QueuebyStack()
    for i in range(5):
        q.appendTail(i)
    while not  q.isEmpty():
        print(q.deleteHead())

    print('stack by queue:\n')
    s=StackbyQueue()
    for i in range(5):
        s.enQueue(i)
    while not s.isEmpty():
        print(s.deQueue())










