# @Time : 2020/3/9 10:15
# @Author : Xylia_Yang
# @Description :找到链表中的中间节点


class TreeNode:
    def __int__(self,data):
        self.val=data
        self.next=None


def SearchMidNode(node):
    if not node:
        return

    slow_p=node
    fast_p=node.next

    while fast_p:
        slow_p=slow_p.next
        fast_p=fast_p.next

        if fast_p:
            fast_p=fast_p.next

    return slow_p

