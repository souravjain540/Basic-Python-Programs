class Queue:
   def __init__(self):
      self.queue = list()

   def addtoq(self,dataval):
# Insert method to add element
   if dataval not in self.queue:
      self.queue.insert(0,dataval)
      return True
   return False

   def size(self):
      return len(self.queue)

TheQueue = Queue()
TheQueue.addtoq("Monday")
TheQueue.addtoq("Tuesday")
TheQueue.addtoq("Wednesday")
TheQueue.addtoq("Thursday")
TheQueue.addtoq("Friday")
print(TheQueue.size())

#Output: 5
