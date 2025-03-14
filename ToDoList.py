import os

# Function to load tasks from a file
def load_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file]
    else:
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to view all tasks
def view_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks to show.")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as complete
def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num] = tasks[task_num] + " (Completed)"
            print(f"Task '{tasks[task_num]}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the application
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_complete(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the application
if __name__ == "__main__":
    main()
