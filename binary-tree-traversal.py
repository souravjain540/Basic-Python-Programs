class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        # Traverse the left subtree
        inorder_traversal(root.left)
        # Visit the root node
        print(root.val, end=' ')
        # Traverse the right subtree
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        # Visit the root node
        print(root.val, end=' ')
        # Traverse the left subtree
        preorder_traversal(root.left)
        # Traverse the right subtree
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        # Traverse the left subtree
        postorder_traversal(root.left)
        # Traverse the right subtree
        postorder_traversal(root.right)
        # Visit the root node
        print(root.val, end=' ')

# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("In-order traversal:")
    inorder_traversal(root)
    print("\nPre-order traversal:")
    preorder_traversal(root)
    print("\nPost-order traversal:")
    postorder_traversal(root)
