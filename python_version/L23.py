# @Time : 2020/3/30 19:48
# @Author : Xylia_Yang
# @Description :

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_1:
    def mergeKLists(self, lists):
        if not lists:
            return

        node=None
        min_node=None
        min_index=-1
        for i in range(len(lists)):
            if not lists[i]:
                continue

            if not min_node:
                min_node=lists[i]
                min_index=i
            else:
                if lists[i].val<min_node.val:
                    min_node=lists[i]
                    min_index=i
        if min_node:
            node = min_node
            lists[min_index] = lists[min_index].next
            node.next = self.mergeKLists(lists)

        return node



class Solution_2:
    def mergeKLists(self, lists):
        if not lists:
            return

        amount=len(lists)
        interval=1

        while interval<amount:
            for i in range(0,amount-interval,interval*2):
                lists[i]=self.mergeSort(lists[i],lists[i+interval])
            interval*=2

        return lists[0]


    def mergeSort(self,list1,list2):
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1


        if list1.val<list2.val:
            node=list1
            node.next=self.mergeSort(list1.next,list2)
        else:
            node=list2
            node.next=self.mergeSort(list1,list2.next)
        return node








if __name__=='__main__':
    solution=Solution_2()
    node1=ListNode(1)
    node1.next=ListNode(4)
    node1.next.next=ListNode(5)

    node2=ListNode(1)
    node2.next=ListNode(3)
    node2.next.next=ListNode(4)

    node3=ListNode(2)
    node3.next=ListNode(6)

    lists=[node1,node2,node3]

    print(solution.mergeKLists(lists))