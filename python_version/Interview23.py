# @Time : 2020/2/23 11:28
# @Author : Xylia_Yang
# @Description : 链表中环的入口节点
# 说明：至少两个才能成环

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def meetingNode(self,head):
        if head is None:
            return None
        pslow=head
        pfast=head.next

        while pfast and pslow:
            if pfast == pslow:
                return pslow

            pslow=pslow.next
            pfast=pfast.next
            if pfast:
                pfast=pfast.next

        return None


    def detectCycle(self, head: ListNode) -> ListNode:
        meet_node=self.meetingNode(head)
        if not meet_node:
            return None

        node_loop=1
        tmp_node=meet_node
        while tmp_node and tmp_node.next!=meet_node:
            node_loop+=1
            tmp_node=tmp_node.next

        pNode1=pNode2=head
        for i in range(node_loop):
            pNode2=pNode2.next

        while  pNode2 !=pNode1 :
            pNode2=pNode2.next
            pNode1=pNode1.next

        return pNode1








