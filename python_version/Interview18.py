
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None


def deleteNode(pHead,pDelete):
    if pHead.next is None or pDelete.next is None:
        pDelete=None
    else:
        pDelete.data=pDelete.next.data
        pDelete.next=pDelete.next.next



