class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if not self.last:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

x = Queue() # Creating object of queue class
x.enqueue(1) # Add 1 to the queue
x.enqueue(2)# Add 2 to the queue
x.display() # 1 => 2
print(x.dequeue()) # Deleting the first element of the queue.
x.display() # 2
print(x.dequeue()) # 2
print(x.dequeue()) # None(because queue is already empty)