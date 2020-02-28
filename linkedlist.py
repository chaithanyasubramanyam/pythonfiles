class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self,previous_node,new_data):
        if previous_node == None:
            print('no')
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.next != None:
                n = n.next
            n.next = new_node  


    def printlist(self):
        n = self.head
        while n != None:
            print(n.data,end = ' ')
            n = n.next


l = [1,2,3,4]
a = Linkedlist()
for i in l:
    a.append(i)
a.printlist()
    


         
