#Contains Binary Tree Preorder , Inorder , PostOrder and Bredth First Traversal Algorithm 

#Expected Node Class
#class Node:
#  def _init_(self , val):
#    self.val = val
#    self.left = None
#    self.return = None

#Preorder Traversal algorithm - > ROOT NODE > LEFT NODE > RIGHT NODE
def preorder_traverse(node):
  if node is not None:
    print(node.val)
    preorder_traverse(node.left)
    preorder_traverse(node.right)

#Inorder Traversal algorithm - > LEFT NODE > ROOT NODE > RIGHT NODE
def inorder_traverse(node):
  if node is not None:
    inorder_traverse(node.left)
    print(node.val)
    inorder_traverse(node.right)

#Postorder Traversal algorithm - > LEFT NODE > RIGHT NODE > ROOT NODE
def postorder_traverse(node):
  if node is not None:
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.val)

#bredth first traversal -> ROOT NODE > LEVEL N LEFT NODE > LEVEL N RIGHT NODE
def bredth_first_traverse(node):
  nodes_list = [node]
  while len(nodes_list)!= 0:
    item = nodes_list.pop(0)
    _traverse_current_node(item , nodes_list)

def _traverse_current_node(node , nodes_list):
  if node is not None:
    print(node.val)
  if node.left is not None:
    nodes_list.append(node.left)
  if node.right is not None:
    nodes_list.append(node.right)
