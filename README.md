# Terminal To-Do List Manager

## Description
The Terminal To-Do List Manager is a robust command-line application designed to streamline task management. This Python-based application allows users to efficiently add, edit, delete, view, and mark tasks as complete, all from the command line. Tasks are organized by priority (high, medium, low) and can be filtered based on their status (completed, pending).

## Features
- **Add Task:** Create a new task with a detailed description, priority level, and due date.
- **Edit Task:** Modify existing task details, including description, priority, and due date.
- **Delete Task:** Remove tasks that are no longer needed.
- **View Tasks:** Display all tasks, with options to filter by status or sort by priority.
- **Mark Task as Complete:** Mark tasks as completed to keep track of progress.
- **Persistent Storage:** Tasks are saved in a JSON file to maintain data between sessions.
- **User-Friendly CLI:** Simple and intuitive command-line interface for managing tasks.

## Installation
### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

Copy code
python project.py
Command-Line Arguments
The application supports several command-line arguments for viewing tasks:

Default View (all tasks):
bash
Copy code
python project.py -v 1
View Pending Tasks:
bash
Copy code
python project.py -v 2
View Completed Tasks:
bash
Copy code
python project.py -v 3
View Tasks by Priority:
bash
Copy code
python project.py -v 4
Interactive Menu
When running without arguments, an interactive menu allows for full task management:

Add Task: Add a new task with a description, priority, and due date.
Edit Task: Edit details of an existing task.
Delete Task: Remove a task from the list.
View Tasks: View all tasks, filtered or sorted by various criteria.
Mark Task as Complete: Mark a task as completed.
Exit: Exit the application.
Project Structure
kotlin
Copy code
todo_manager/
├── project.py
├── test_project.py
├── requirements.txt
└── data/
    └── tasks.json
File Descriptions
project.py: Contains the main application code, including functions for adding, editing, deleting, viewing, and marking tasks as complete.
test_project.py: Contains unit tests for the application's functions, ensuring they work as expected.
requirements.txt: Lists the dependencies required to run the application.
data/tasks.json: Stores tasks in JSON format, ensuring persistence between sessions.
Functions
Main Function
main()
Runs the command-line interface, parses arguments, and displays the interactive menu.

Task Management Functions
add_task()
Prompts the user for task details and adds a new task to the list.

edit_task()
Allows the user to select and edit an existing task's details.

delete_task()
Enables the user to delete a specified task from the list.

view_tasks()
Displays all tasks, with options to filter by status or sort by priority.

mark_task_complete()
Marks a selected task as completed.

Helper Functions
load_tasks()
Loads tasks from the JSON file.

save_tasks()
Saves tasks to the JSON file.

view(v)
Displays tasks based on the specified view option.

Testing
Running Tests
To run the tests using pytest, execute:

bash
Copy code
pytest
Test Cases
test_add_task: Verifies that tasks are added correctly.
test_edit_task: Ensures that tasks can be edited correctly.
test_save_task: Confirms that tasks are saved correctly.
test_delete_task: Validates that tasks are deleted correctly.

Future Enhancements
Data Persistence: Upgrade to a more robust database solution like SQLite.
Task Reminders: Add functionality to set reminders for tasks.
Enhanced Filtering: Improve task filtering options with additional criteria like tags.
User Authentication: Implement user authentication for managing tasks independently.
Graphical User Interface: Develop a GUI version for users who prefer a visual interface.
Mobile Application: Create a mobile app for on-the-go task management.
