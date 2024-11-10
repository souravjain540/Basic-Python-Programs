class Stack:
    def __init__(self):
        """Initialize an empty list to act as the stack"""
        self.stack = []

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")
        

    def pop(self):
        """Pop the top item from the stack. Return None if stack is empty."""
        if not self.is_empty():
            popped_item = self.stack.pop()
            print(f"Popped item: {popped_item}")
            return popped_item
        else:
            print("Stack is empty! Cannot pop.")
            return None

    def peek(self):
        """Return the top item of the stack without removing it. Return None if stack is empty."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty!")
            return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

    def print_stack(self):
        """Print the current state of the stack in a readable format."""
        if self.stack:
            print("Stack: ",list(self.stack))
                
        else:
            print("Stack is empty!")

# Main function to handle user input
def main():
    stack = Stack()

    print("Choose an operation:")
    print("1. Push an element onto the stack")
    print("2. Pop an element from the stack")
    print("3. Peek at the top element")
    print("4. Check if the stack is empty")
    print("5. Get the stack size")
    print("6. Display the stack")
    print("7. Exit")

    while True:
        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            element = input("Enter the item to push: ")
            stack.push(element)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            top = stack.peek()
            if top is not None:
                print(f"Top element: {top}")
        elif choice == '4':
            if stack.is_empty():
                print("The stack is empty.")
            else:
                print("The stack is not empty.")
        elif choice == '5':
            print(f"Stack size: {stack.size()}")
        elif choice == '6':
            stack.print_stack()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please choose a valid option.")

# Run the program
if __name__ == "__main__":
    main()
