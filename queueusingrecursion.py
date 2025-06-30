class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return None
        return self._dequeue_recursive(0)

    def _dequeue_recursive(self, index):
        if index == len(self.items) - 1:
            return self.items.pop(0)
        self.items[index] = self.items[index + 1]
        return self._dequeue_recursive(index + 1)

    def peek(self):
        if not self.items:
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print(q.dequeue())
q.display()
