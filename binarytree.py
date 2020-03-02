class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

class Binarytree:
    def __init__(self):
        self.root = None
    
    def insert(self,temp,data):
        q = []
        q.append(temp)

        while len(q) != 0:
            temp = q[0]
            q.pop(0)

            if temp.left == None:
                temp.left = Node(data)
                break
            else:
                q.append(temp.left)
            if temp.right == None:
                temp.right = Node(data)
                break
            else:
                q.append(temp.right)
        
    def printbfs(self,temp):
        q = []
        q.append(temp)
        while len(q) != 0:
            temp = q[0]
            q.pop(0)

            print(temp.data,end=' ')
            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)











def inorder(temp):
    if temp == None:
        return
    else:
        inorder(temp.left)
        print(temp.data,end=' ')
        inorder(temp.right)

tree = Binarytree()
tree.root = Node(10)
tree.root.left = Node(11)  
tree.root.left.left = Node(7)  
tree.root.right = Node(9)  
tree.root.right.left = Node(15)  
tree.root.right.right = Node(8)
tree.insert(tree.root,12)
inorder(tree.root)
tree.printbfs(tree.root)





