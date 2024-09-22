import pytest
from todo_manager import load_tasks, save_tasks

def test_add_task():
    # Prepare a temporary tasks list
    tasks = load_tasks()
    original_len = len(tasks)
    
    # Add a new task
    task = {
        "description": "Test Task 1",
        "priority": "medium",
        "due_date": "2024-12-31",
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    
    # Reload tasks and check if the new task was added
    tasks = load_tasks()
    assert len(tasks) == original_len + 1
    assert tasks[-1] == task


def test_edit_task():
    # Prepare a temporary tasks list
    tasks = load_tasks()
    if not tasks:
        pytest.skip("No tasks available to edit.")
        
    # Edit the first task
    tasks[0]["description"] = "Updated Task"
    save_tasks(tasks)
    
    # Reload tasks and check if the task was updated
    tasks = load_tasks()
    assert tasks[0]["description"] == "Updated Task"


def test_save_task():
    # Prepare a temporary tasks list
    tasks = load_tasks()
    original_len = len(tasks)

    # Add a new task
    task = {
        "description": "Test Task 2",
        "priority": "high",
        "due_date": "2024-12-31",
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)

    # Reload tasks and check if the new task was added
    tasks = load_tasks()
    assert len(tasks) == original_len + 1
    assert tasks[-1] == task
    
    
def test_delete_task():
    # Prepare a temporary tasks list
    tasks = load_tasks()
    original_len = len(tasks)
    if not tasks:
        pytest.skip("No tasks available to delete.")
    
    # Delete the second task
    tasks.pop(1)
    # Delete the first task
    tasks.pop(0)
    save_tasks(tasks)
    
    # Reload tasks and check if the task was deleted
    tasks = load_tasks()
    assert len(tasks) == original_len - 2