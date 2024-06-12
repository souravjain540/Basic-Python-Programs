
# Python implementation of algorithm to remove duplicates
# from an unsorted doubly linked list. Here the outer loop
# is used to pick the elements one by one and the inner
# loop compares the picked element with the rest of the
# elements. Time complexity: O(n^2) and auxiliary space
# 0(1)

# Node of a linked list
class Node:
	def __init__(self, data = None, next = None):
		self.next = next
		self.data = data

# Function to delete a node in a Doubly Linked List.
# head_ref -. pointer to head node pointer.
# del -. pointer to node to be deleted.
def deleteNode(head_ref,del_):

	# base case
	if (head_ref == None or del_ == None):
		return head_ref

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
def removeDuplicates( head_ref):

	# if DLL is empty or if it contains only
	# a single node
	if ((head_ref) == None or (head_ref).next == None):
		return head_ref

	ptr1 = head_ref
	ptr2 = None

	# pick elements one by one
	while(ptr1 != None) :
		ptr2 = ptr1.next

		# Compare the picked element with the
		# rest of the elements
		while (ptr2 != None):
		
			# if duplicate, then delete it
			if (ptr1.data == ptr2.data):
			
				# store pointer to the node next to 'ptr2'
				next = ptr2.next

				# delete node pointed to by 'ptr2'
				head_ref = deleteNode(head_ref, ptr2)

				# update 'ptr2'
				ptr2 = next

			# else simply move to the next node
			else:
				ptr2 = ptr2.next
		ptr1 = ptr1.next
	return head_ref

# Function to insert a node at the beginning
# of the Doubly Linked List
def push( head_ref, new_data):

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

# Function to print nodes in a
# given doubly linked list
def printList( head):

	# if list is empty
	if (head == None):
		print("Doubly Linked list empty")

	while (head != None):
		print( head.data ,end= " ")
		head = head.next
	
# Driver Code
head = None

# Create the doubly linked list:
# 8<.4<.4<.6<.4<.8<.4<.10<.12<.12
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

# remove duplicate nodes */
head=removeDuplicates(head)

print("\nDoubly linked list after removing duplicates:")
printList(head)


