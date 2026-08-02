class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

def inOrder(root):
     if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


root = Node(1)
root.left = Node(3)
root.right = Node(5)

root.left.left = Node(2)
root.left.right = Node(4)

root.right.right = Node(8)

inOrder(root)