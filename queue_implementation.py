"""
Queue Implementation - FIFO (First In First Out) data structure
Common operations: enqueue, dequeue, peek, is_empty, size
"""

class Queue:
    """Queue implementation using Python list"""
    
    def __init__(self):
        """Initialize an empty queue"""
        self.items = []
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue
        
        Args:
            item: Item to add to queue
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the front item from the queue
        
        Returns:
            Front item, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        """
        Return the front item without removing it
        
        Returns:
            Front item, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self):
        """
        Check if queue is empty
        
        Returns:
            True if empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of items in queue
        
        Returns:
            Number of items
        """
        return len(self.items)
    
    def display(self):
        """Display all items in the queue"""
        if self.is_empty():
            print("Queue is empty")
        else:
            print(f"Queue (front to rear): {self.items}")


class CircularQueue:
    """Circular Queue implementation with fixed size"""
    
    def __init__(self, capacity):
        """
        Initialize circular queue with given capacity
        
        Args:
            capacity: Maximum number of items
        """
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.count == 0
    
    def is_full(self):
        """Check if queue is full"""
        return self.count == self.capacity
    
    def enqueue(self, item):
        """Add item to circular queue"""
        if self.is_full():
            print("Queue is full!")
            return False
        
        if self.front == -1:
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.count += 1
        return True
    
    def dequeue(self):
        """Remove and return front item"""
        if self.is_empty():
            return None
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        self.count -= 1
        return item
    
    def display(self):
        """Display queue contents"""
        if self.is_empty():
            print("Circular Queue is empty")
        else:
            print(f"Circular Queue: {[x for x in self.queue if x is not None]}")


class PriorityQueue:
    """Priority Queue implementation (min-heap based)"""
    
    def __init__(self):
        """Initialize an empty priority queue"""
        self.items = []
    
    def enqueue(self, item, priority):
        """
        Add item with priority
        
        Args:
            item: Item to add
            priority: Priority (lower number = higher priority)
        """
        self.items.append((priority, item))
        self.items.sort()
    
    def dequeue(self):
        """Remove and return highest priority item"""
        if self.is_empty():
            return None
        return self.items.pop(0)[1]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def display(self):
        """Display queue with priorities"""
        if self.is_empty():
            print("Priority Queue is empty")
        else:
            print("Priority Queue (priority, item):")
            for priority, item in self.items:
                print(f"  ({priority}, {item})")


if __name__ == "__main__":
    print("=" * 50)
    print("QUEUE DATA STRUCTURE DEMONSTRATION")
    print("=" * 50)
    
    # 1. Basic Queue
    print("\n1. Basic Queue (FIFO):")
    q = Queue()
    
    q.enqueue("First")
    q.enqueue("Second")
    q.enqueue("Third")
    q.enqueue("Fourth")
    
    q.display()
    print(f"Front item: {q.peek()}")
    print(f"Size: {q.size()}")
    
    print(f"\nDequeued: {q.dequeue()}")
    print(f"Dequeued: {q.dequeue()}")
    q.display()
    
    # 2. Circular Queue
    print("\n" + "=" * 50)
    print("2. Circular Queue:")
    cq = CircularQueue(5)
    
    print("\nEnqueuing 1, 2, 3, 4, 5:")
    for i in range(1, 6):
        cq.enqueue(i)
    cq.display()
    
    print(f"\nQueue full? {cq.is_full()}")
    cq.enqueue(6)  # Should fail
    
    print(f"\nDequeued: {cq.dequeue()}")
    print(f"Dequeued: {cq.dequeue()}")
    cq.display()
    
    print("\nEnqueuing 6, 7:")
    cq.enqueue(6)
    cq.enqueue(7)
    cq.display()
    
    # 3. Priority Queue
    print("\n" + "=" * 50)
    print("3. Priority Queue:")
    pq = PriorityQueue()
    
    pq.enqueue("Low priority task", 5)
    pq.enqueue("High priority task", 1)
    pq.enqueue("Medium priority task", 3)
    pq.enqueue("Critical task", 0)
    
    pq.display()
    
    print("\nProcessing tasks by priority:")
    while not pq.is_empty():
        print(f"  Processing: {pq.dequeue()}")
    
    # 4. Real-world example: Print Queue
    print("\n" + "=" * 50)
    print("4. Print Queue Simulation:")
    
    print_queue = Queue()
    print_queue.enqueue("Document1.pdf")
    print_queue.enqueue("Image.png")
    print_queue.enqueue("Report.docx")
    
    print("\nPrint queue:")
    print_queue.display()
    
    print("\nPrinting documents:")
    while not print_queue.is_empty():
        doc = print_queue.dequeue()
        print(f"  Printing: {doc}")
    
    print("\nAll documents printed!")
    print_queue.display()
    
    # Interactive menu
    print("\n" + "=" * 50)
    print("5. Interactive Queue:")
    user_queue = Queue()
    
    while True:
        print("\nOptions:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        try:
            choice = input("\nEnter choice (1-5): ")
            
            if choice == '1':
                item = input("Enter item to enqueue: ")
                user_queue.enqueue(item)
                print(f"Enqueued: {item}")
            elif choice == '2':
                item = user_queue.dequeue()
                if item:
                    print(f"Dequeued: {item}")
                else:
                    print("Queue is empty!")
            elif choice == '3':
                item = user_queue.peek()
                if item:
                    print(f"Front item: {item}")
                else:
                    print("Queue is empty!")
            elif choice == '4':
                user_queue.display()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
