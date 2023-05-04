# Python3 implementation of algorithm to remove duplicates
# from an unsorted doubly linked list. This approach is
# obviously more efficent. The doubly linked list is
# traversed from head to tail. For every newly encountered
# element, check whether it is in the hash table. If yes,
# it is removed. Otherwise we put it in the hash table.
# Time complexity is O(n) and space O(n).

# a node of the doubly linked list
class Node:
	def __init__(self):
		self.data = 0
		self.next = None
		self.prev = None

# Function to delete a node in a Doubly Linked List.
# head_ref --> pointer to head node pointer.
# del --> pointer to node to be deleted.
def deleteNode( head_ref, del_):

	# base case
	if (head_ref == None or del_ == None):
		return None

	# If node to be deleted is head node
	if (head_ref == del_):
		head_ref = del_.next

	# Change next only if node to be deleted
	# is NOT the last node
	if (del_.next != None):
		del_.next.prev = del_.prev

	# Change prev only if node to be deleted
	# is NOT the first node
	if (del_.prev != None):
		del_.prev.next = del_.next

	return head_ref

# function to remove duplicates from
# an unsorted doubly linked list
def removeDuplicates(head_ref):

	# if doubly linked list is empty
	if ((head_ref) == None):
		return None

	# unordered_set 'us' implemented as hash table
	us = set()

	current = head_ref
	next = None

	# traverse up to the end of the list
	while (current != None):
	
		# if current data is seen before
		if ((current.data) in us):
		
			# store pointer to the node next to
			# 'current' node
			next = current.next

			# delete the node pointed to by 'current'
			head_ref = deleteNode(head_ref, current)

			# update 'current'
			current = next
		
		else:
	
			# insert the current data in 'us'
			us.add(current.data)

			# move to the next node
			current = current.next
	
	return head_ref

# Function to insert a node at the
# beginning of the Doubly Linked List
def push(head_ref,new_data):

	# allocate node
	new_node = Node()

	# put in the data
	new_node.data = new_data

	# since we are adding at the beginning,
	# prev is always None
	new_node.prev = None

	# link the old list of the new node
	new_node.next = (head_ref)

	# change prev of head node to new node
	if ((head_ref) != None):
		(head_ref).prev = new_node

	# move the head to point to the new node
	(head_ref) = new_node
	return head_ref

# Function to print nodes in a given doubly
# linked list
def printList( head):

	# if list is empty
	if (head == None):
		print("Doubly Linked list empty")

	while (head != None):
	
		print(head.data , end=" ")
		head = head.next
	
# Driver Code

head = None

# Create the doubly linked list:
# 8<->4<->4<->6<->4<->8<->4<->10<->12<->12
head = push(head, 12)
head = push(head, 12)
head = push(head, 10)
head = push(head, 4)
head = push(head, 8)
head = push(head, 4)
head = push(head, 6)
head = push(head, 4)
head = push(head, 4)
head = push(head, 8)

print("Original Doubly linked list:")
printList(head)

# remove duplicate nodes
head = removeDuplicates(head)

print("\nDoubly linked list after removing duplicates:")
printList(head)



