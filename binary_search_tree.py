class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def binsert(root, data):
    if root is None:
        return Node(data)

    if data < root.value:
        root.left = binsert(root.left, data)
    elif data > root.value:
        root.right = binsert(root.right, data)    
    else:
        print(f"{data} already exists")
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

b = Node(100)
print("Root Node:",b.value)
binsert(b, 30)
binsert(b, 3)
binsert(b, 200)
binsert(b, 10)
print("Inorder of Traversal of the tree:")
inorder(b)