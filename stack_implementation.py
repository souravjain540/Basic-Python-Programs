"""
Stack Implementation - LIFO (Last In First Out) data structure
Common operations: push, pop, peek, is_empty, size
"""

class Stack:
    """Stack implementation using Python list"""
    
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack
        
        Args:
            item: Item to push onto stack
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack
        
        Returns:
            Top item, or None if stack is empty
        """
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        """
        Return the top item without removing it
        
        Returns:
            Top item, or None if stack is empty
        """
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if stack is empty
        
        Returns:
            True if empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of items in stack
        
        Returns:
            Number of items
        """
        return len(self.items)
    
    def display(self):
        """Display all items in the stack"""
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (top to bottom):")
            for item in reversed(self.items):
                print(f"  {item}")


def reverse_string(text):
    """
    Reverse a string using stack
    
    Args:
        text: String to reverse
    
    Returns:
        Reversed string
    """
    stack = Stack()
    for char in text:
        stack.push(char)
    
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return reversed_text


def is_balanced_parentheses(expression):
    """
    Check if parentheses in expression are balanced
    
    Args:
        expression: String containing parentheses
    
    Returns:
        True if balanced, False otherwise
    """
    stack = Stack()
    opening = "({["
    closing = ")}]"
    matches = {"(": ")", "{": "}", "[": "]"}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if matches[stack.pop()] != char:
                return False
    
    return stack.is_empty()


def decimal_to_binary(number):
    """
    Convert decimal to binary using stack
    
    Args:
        number: Decimal number
    
    Returns:
        Binary representation as string
    """
    if number == 0:
        return "0"
    
    stack = Stack()
    while number > 0:
        stack.push(number % 2)
        number //= 2
    
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
    
    return binary


if __name__ == "__main__":
    print("=" * 50)
    print("STACK DATA STRUCTURE DEMONSTRATION")
    print("=" * 50)
    
    # Basic stack operations
    stack = Stack()
    
    print("\n1. Basic Operations:")
    print(f"Is empty? {stack.is_empty()}")
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
    print(f"\nAfter pushing 10, 20, 30, 40:")
    stack.display()
    
    print(f"\nPeek: {stack.peek()}")
    print(f"Size: {stack.size()}")
    
    print(f"\nPopped: {stack.pop()}")
    stack.display()
    
    # String reversal
    print("\n" + "=" * 50)
    print("2. String Reversal Using Stack:")
    text = "Hello, World!"
    reversed_text = reverse_string(text)
    print(f"Original: {text}")
    print(f"Reversed: {reversed_text}")
    
    # Balanced parentheses
    print("\n" + "=" * 50)
    print("3. Balanced Parentheses Checker:")
    expressions = [
        "{[()]}",
        "{[(])}",
        "((()))",
        "((())",
        "{[}]"
    ]
    
    for expr in expressions:
        result = "Balanced" if is_balanced_parentheses(expr) else "Not Balanced"
        print(f"{expr}: {result}")
    
    # Decimal to binary
    print("\n" + "=" * 50)
    print("4. Decimal to Binary Conversion:")
    numbers = [10, 25, 42, 100]
    for num in numbers:
        binary = decimal_to_binary(num)
        print(f"{num} = {binary}")
    
    # Interactive menu
    print("\n" + "=" * 50)
    print("5. Interactive Stack:")
    user_stack = Stack()
    
    while True:
        print("\nOptions:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        try:
            choice = input("\nEnter choice (1-5): ")
            
            if choice == '1':
                item = input("Enter item to push: ")
                user_stack.push(item)
                print(f"Pushed: {item}")
            elif choice == '2':
                item = user_stack.pop()
                if item:
                    print(f"Popped: {item}")
                else:
                    print("Stack is empty!")
            elif choice == '3':
                item = user_stack.peek()
                if item:
                    print(f"Top item: {item}")
                else:
                    print("Stack is empty!")
            elif choice == '4':
                user_stack.display()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
