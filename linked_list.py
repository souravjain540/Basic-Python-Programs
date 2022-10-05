class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_begin(self, data):
        new_node = Node(data)           
        new_node.ref = self.head
        self.head = new_node            

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, after, data):
        n = self.head

        while n is not None:
            if n.data == after:
                break
            else:
                n = n.ref
        
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def printl2(self):
        if self.head is None:
            print("Linked List is empty")
        
        else:
            n = self.head
            while n is not None:
                print(n.data, '-->', end = ' ')
                n = n.ref

    def del_begin(self):
        if self.head is None:
            print("delete operation is not possible")
        else:
            self.head = self.head.ref
        
    def del_end(self):
        if self.head is None:
            print("delete operation is not possible")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def del_node(self, node):
        if self.head == None:
            print("deletion operation is not possibe")
        elif self.head.data == node:
            self.del_begin()
        else:    
            n = self.head
            while n.ref is not None:
                if n.ref.data == node:
                    break
                else:
                    n = n.ref
            
            if n.ref is None:
                print("Can't delete a node that doesn't exist")
            else:
                n.ref = n.ref.ref


l = LinkedList()
l.add_begin(10)
l.add_begin(5)
l.add_begin(1)
l.add_end(15)
l.add_after(5, 12)
l.add_after(10, 0)
l.printl2()
print("")
l.del_begin()
l.del_end()
l.del_node(12)
l.printl2()