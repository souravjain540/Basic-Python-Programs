
import requests
import json
from datetime import datetime

# Function to fetch a random motivational quote
def fetch_quote():
    fallback_quote = "'Stay positive, work hard, make it happen.' - Unknown"
    url = "https://zenquotes.io/api/random"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            quote_data = response.json()
            if len(quote_data) > 0:
                quote = quote_data[0]
                return f"'{quote['q']}' - {quote['a']}"
            else:
                return fallback_quote
        else:
            return fallback_quote
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return fallback_quote

# Function to create a daily task planner
def task_planner():
    tasks = []
    print("Enter your tasks for the day (type 'done' to finish):")
    
    while True:
        task = input("> ")
        if task.lower() == 'done':
            break
        tasks.append(task)
    
    return tasks

# Function to save tasks to a file
def save_tasks(date, tasks):
    planner = {"date": date, "tasks": tasks}
    with open(f"tasks_{date}.json", 'w') as file:
        json.dump(planner, file, indent=4)

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"\nToday's Date: {today}")
    
    # Fetch and display a motivational quote
    quote = fetch_quote()
    print(f"\nDaily Motivation: {quote}\n")
    
    # Collects the tasks from the user
    tasks = task_planner()
    
    # Saves the tasks to a file
    if tasks:
        save_tasks(today, tasks)
        print("\nYour tasks have been saved!\n")
    else:
        print("No tasks to save.\n")

if __name__ == "__main__":
    main()