class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DDl:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        if temp is None:
            print("the list is empty")
        else:
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next


dl=DDl()
n1=Node(10)
dl.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
dl.display()
