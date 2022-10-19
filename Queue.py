class Queue:
    arr = []
    def enqueue(self,item):
        self.arr.append(item)
    
    def dequeue(self):
        if len(self.arr) > 0:
            ditem = self.arr[0] 
            del self.arr[0]
            return ditem
        else:
            return #queue is empty
    
    def dispaly(self):
        print(self.arr)

x = Queue() # Creating object of queue class
x.enqueue(1) 
x.enqueue(2) 
x.dispaly() # arr = [1,2]
x.dequeue() # Deleting the first element of the queue.
x.dispaly() # arr = [2]
print(x.dequeue()) # 2
print(x.dequeue()) # None(because queue is already empty)