# This file contains the implementation of a singly linked list and a doubly linked list in Python

# Implementation of linked list in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)
    
    def insert(self, data):
        if self.next is None:
            self.next = Node(data) 
        else:
            self.next.insert(data) 
    
    def delete(self, data):
        if self.next is None:
            return False
        elif self.next.data == data:
            self.next = self.next.next
            return True
        else:
            return self.next.delete(data)
    
    def print(self):
        print(self.data)
        if self.next is not None:
            self.next.print()
    
    def search(self, data):
        if self.data == data:
            return True
        elif self.next is None:
            return False
        else:
            return self.next.search(data)
    
    def reverse(self):
        if self.next is None:
            return self
        else:
            reversed = self.next.reverse()
            self.next.next = self
            self.next = None
            return reversed

# Implementation of doubly linked list

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self) -> str:
        return str(self.data)
    
    def insert(self, data):
        if self.next is None:
            self.next = DoublyNode(data)
            self.next.prev = self
        else:
            self.next.insert(data)
    
    def delete(self, data):
        if self.next is None:
            return False
        elif self.next.data == data:
            self.next = self.next.next
            self.next.prev = self
            return True
        else:
            return self.next.delete(data)
    
    def print(self):
        print(self.data)
        if self.next is not None:
            self.next.print()
    
    def search(self, data):
        if self.data == data:
            return True
        elif self.next is None:
            return False
        else:
            return self.next.search(data)
    
    def reverse(self):
        if self.next is None:
            return self
        else:
            next = self.next
            self.next = self.prev
            self.prev = next
            return next.reverse()

# Menu driven program to test the linked list implementation

def menu():
    print("1. Insert")
    print("2. Delete")
    print("3. Print")
    print("4. Search")
    print("5. Reverse")
    print("6. Exit")
    return int(input("Enter your choice: "))

def mainMenu():
    # ask user to enter the type of linked list

    print("1. Singly Linked List")
    print("2. Doubly Linked List")
    choice = int(input("Enter your choice: "))

    # 0 is the head of the linked list

    if choice == 1:
        node = Node(0)
    elif choice == 2:
        node = DoublyNode(0)
    else:
        print("Invalid choice")
        return

    while True:
        choice = menu()
        if choice == 1:
            data = int(input("Enter the data: "))
            node.insert(data)
        elif choice == 2:
            data = int(input("Enter the data: "))
            if node.delete(data):
                print("Deleted")
            else:
                print("Not found")
        elif choice == 3:
            node.print()
        elif choice == 4:
            data = int(input("Enter the data: "))
            if node.search(data):
                print("Found")
            else:
                print("Not found")
        elif choice == 5:
            node = node.reverse()
        elif choice == 6:
            break
        else:
            print("Invalid choice")

mainMenu()