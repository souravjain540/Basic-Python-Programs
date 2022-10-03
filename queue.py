from collections import deque
queue = deque()

def enqueue():
    x = input("Enter an element: ")
    queue.append(x)
    print(list(queue))

def dq():
    if not queue:
        print("Can't perform pop on empty queue.")
    else:
        print("Popped element: ", queue.popleft())
        print(list(queue))

while True:
    ch = int(input("1.enqueue, 2. dequeue, 3. quit \nEnter: "))
    if ch == 1:
        enqueue()
    elif ch == 2:
        dq()
    elif ch == 3:
        break
    else:
        print("Invalid operation!")