class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        self.length=1
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def middle_Node(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.value


ll=LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
#ll.append(7)

print(ll.middle_Node())