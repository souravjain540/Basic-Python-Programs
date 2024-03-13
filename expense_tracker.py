import json
from datetime import datetime

# Expense Tracker CLI Application

# File to store the expense data
DATA_FILE = 'expenses.json'

# Load expenses from the file
def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to the file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    category = input("Enter the expense category: ")
    amount = float(input("Enter the expense amount: "))
    description = input("Enter the expense description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expenses.append({"category": category, "amount": amount, "description": description, "date": date})
    save_expenses(expenses)
    print("Expense added successfully.")

# List all expenses
def list_expenses(expenses):
    for expense in expenses:
        print(f"Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}, Date: {expense['date']}")

# Main function
def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker CLI")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            list_expenses(expenses)
        elif choice == '3':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
