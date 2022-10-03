stack = []

def push():
    x = input("Enter an element: ")
    stack.append(x)
    print(stack)

def pop_():
    if not stack:
        print("Can't perform pop on empty stack.")
    else:
        print("Popped element ", stack.pop())
        print(stack)

while True:
    ch = int(input("1.push, 2. pop, 3. quit \nEnter: "))
    if ch == 1:
        push()
    elif ch == 2:
        pop_()
    elif ch == 3:
        break
    else:
        print("Invalid operation!")