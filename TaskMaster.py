import json
import os
from datetime import datetime

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to create a new task management system
def create_task_manager():
    clear_screen()
    task_manager = {"tasks": []}
    with open("task_manager.json", "w") as file:
        json.dump(task_manager, file)
    print("The task management system has been created.")

# Function to add a task
def add_task():
    clear_screen()
    task_name = input("Enter the task name: ")
    task_description = input("Enter the task description: ")
    task_due_date = input("Enter the due date (YYYY-MM-DD) of the task: ")
    task_priority = input("Enter the priority of the task (High/Medium/Low): ")

    try:
        with open("task_manager.json", "r") as file:
            task_manager = json.load(file)
        task_manager["tasks"].append({
            "name": task_name,
            "description": task_description,
            "due_date": task_due_date,
            "priority": task_priority,
            "status": "Open"
        })
        with open("task_manager.json", "w") as file:
            json.dump(task_manager, file)
        print("The task has been added.")
    except FileNotFoundError:
        print("The task management system was not found.")

# Function to view all tasks
def view_tasks():
    clear_screen()
    try:
        with open("task_manager.json", "r") as file:
            task_manager = json.load(file)
        print("Tasks:")
        for index, task in enumerate(task_manager["tasks"], start=1):
            print(f"{index}. {task['name']} (Due on: {task['due_date']}, Priority: {task['priority']}, Status: {task['status']})")
    except FileNotFoundError:
        print("The task management system was not found.")

# Function to update the status of a task
def update_task_status():
    clear_screen()
    try:
        with open("task_manager.json", "r") as file:
            task_manager = json.load(file)
        view_tasks()
        task_index = int(input("Enter the number of the task you want to update: ")) - 1
        if 0 <= task_index < len(task_manager["tasks"]):
            new_status = input("Enter the new status of the task (Open/In Progress/Done): ")
            task_manager["tasks"][task_index]["status"] = new_status
            with open("task_manager.json", "w") as file:
                json.dump(task_manager, file)
            print("The task status has been updated.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("The task management system was not found.")

# Main menu of the application
def main_menu():
    while True:
        clear_screen()
        print("Welcome to the Task Management System!")
        print("1. Create a new task management system")
        print("2. Add a task")
        print("3. View tasks")
        print("4. Update task status")
        print("5. Exit")
        choice = input("Please select an option: ")
        if choice == "1":
            create_task_manager()
            input("Press Enter to continue...")
        elif choice == "2":
            add_task()
            input("Press Enter to continue...")
        elif choice == "3":
            view_tasks()
            input("Press Enter to continue...")
        elif choice == "4":
            update_task_status()
            input("Press Enter to continue...")
        elif choice == "5":
            break

if __name__ == "__main__":
    main_menu()
