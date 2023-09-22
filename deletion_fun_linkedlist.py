class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def  insert_at_begin(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def inser_at_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def insert_at_pos(self,data,pos):
        if(pos==1):
           self.insert_at_begin(data)
        else:
           np=Node(data)
           temp=self.head
        
      
           for i in range(1,pos-1):
             temp=temp.next
           np.next=temp.next
           temp.next=np
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
        
    def  delete_at_begin(self):
        temp=self.head
        self.head=temp.next
        temp=None
    def delete_at_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_at_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
        print()
        
l=LinkedList()
n=Node(2)
l.head=n
n1=Node(20)
n2=Node(15)
n3=Node(10)
n.next=n1
n1.next=n2
n2.next=n3
l.insert_at_begin(1)
l.insert_at_begin(5)
l.inser_at_end(40)
l.inser_at_end(30)
l.insert_at_pos(7,3)
l.display()
l.delete_at_begin()
l.delete_at_end()
l.delete_at_pos(3)
l.display()



