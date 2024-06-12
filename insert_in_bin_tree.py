# Python progran to demonstrate
# insertion in binary search tree


class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key


# a utiity function to insert
# a new node with the given key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
            
    return root

# a utility function to print inorder
# traversal of BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# driver code to test the above functions
# Let's create the following BST
#      50
#      /  \
#    30   70
#     /\  /\ 
#   20  40  60 80

r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)

inorder(r)

