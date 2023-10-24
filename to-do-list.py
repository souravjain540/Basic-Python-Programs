# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added to the to-do list.")

# Function to view the to-do list
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Function to remove a task from the to-do list
def remove_task():
    view_tasks()
    task_index = int(input("Enter the number of the task to remove: "))
    
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task number. No task removed.")

# Main program loop
while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
