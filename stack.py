class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self, value):
        newNode=Node(value)
        self.top=newNode
        self.height=1

    def push(self,value):
        newNode=Node(value)
        if self.height==0:
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode 
        self.height+=1

    def pop(self):
        if self.top is None:
            return
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.height-=1

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next


st=Stack(1)
st.push(2)
st.push(3)
st.pop()
st.push(4)
st.print_stack()
