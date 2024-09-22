import argparse
import json

from datetime import datetime

DATA_FILE = 'data/tasks.json'

def main():
    parser = argparse.ArgumentParser(description="To-Do List Manager")
    parser.add_argument("-v", help=f"how to view the tasks:1.default view  \
        2.to view pending tasks  3.to view completed tasks  \
        4.to view tasks based on their priority", type=int)
    args = parser.parse_args()
    
    if args.v != None:
            view(args.v)
            print("." * 20)
            return
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Mark Task as Complete")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                add_task()
            case 2:
                edit_task()
            case 3:
                delete_task()
            case 4:
                view_tasks()
            case 5:
                mark_task_complete()
            case 6:
                print("Exited...")
                break
            case _:
                print("Invalid choice. Please try again.")
        print("_" * 20)


def add_task():
    description = input("Enter task description: ")
    while True:
        priority = input("Enter task priority (low, medium, high): ")
        if priority == "low" or priority == "medium" or priority == "high":
            break
    due_date = input("Enter due date (YYYY-MM-DD): ")

    task = {
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


def edit_task():
    view_tasks()
    task_id = int(input("Enter task ID to edit: ")) - 1

    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        description = input("Enter new task description: ")
        priority = input("Enter new task priority (low, medium, high): ")
        due_date = input("Enter new due date (YYYY-MM-DD): ")

        tasks[task_id].update({
            "description": description,
            "priority": priority,
            "due_date": due_date
        })
        save_tasks(tasks)
        print("Task edited successfully!")
    else:
        print("Invalid task ID.")


def delete_task():
    view_tasks()
    task_id = int(input("Enter task ID to delete: ")) - 1

    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task ID.")


def view_tasks():
    tasks = load_tasks()
    print("\nTasks:")
    if not tasks:
        print("No tasks available.")
        return

    # idx - index
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['description']} - {task['priority']} priority - Due {task['due_date']} - {status}")                    
   
                    
def mark_task_complete():
    view_tasks()
    task_id = int(input("Enter task ID to mark as complete: ")) - 1

    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task ID.")


def load_tasks():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
    
    
def view(v):
    tasks = load_tasks()
    
    # default view
    if v == 1:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['description']} - {task['priority']} priority - Due {task['due_date']} - {status}")        
    # to view pending tasks
    elif v == 2:
        for index, task in enumerate(tasks, start=1):
            if not task["completed"]:
                print(f"{index}. {task['description']} - {task['priority']} priority - Due {task['due_date']}")
    # to view completed tasks
    elif v == 3:
        for index, task in enumerate(tasks, start=1):
            if task["completed"]:
                print(f"{index}. {task['description']} - {task['priority']} priority - Due {task['due_date']}")
    # to view tasks based on priority:
    elif v == 4:
        priorities = ["high", "medium", "low"]
        for priority in priorities:
            print(f"\n{priority.capitalize()} Priority tasks:")
            for task in tasks:
                if task["priority"] == priority:
                    status = "Completed" if task["completed"] else "Pending"
                    print(f"{task['description']} - {task['priority']} priority - Due {task['due_date']} - {status}")


if __name__ == "__main__":
    main()
