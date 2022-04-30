class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            else:
                if data>self.data:
                    if self.right is None:
                        self.right=Node(data)
                    else:
                        self.right.insert(data)
        else:
            self.data=data
    def findval(self,search):
        if search<self.data:
            if self.left is None:
                return str(search)+" Not Found"
            return self.left.findval(search)
        elif search>self.data:
            if self.right is None:
                return str(search)+" Not Found"
            return self.right.findval(search)
        else:
            return(str(self.data)+" is Found")
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print (self.data)
        if self.right:
            self.right.PrintTree()

#Function to print Inorder Traversal
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)

def printPreorder(root):
    if root:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)

# In Main
root=Node(12)
root.insert(6)
root.insert(12)
root.insert(32)
root.insert(7)
print(root.findval(17))
print(root.findval(32))
root.PrintTree()
print("Inorder Traversal")
printInorder(root)
print("Preorder Traversal")
printPreorder(root)
print("Postorder Traversal")
printPostorder(root)
