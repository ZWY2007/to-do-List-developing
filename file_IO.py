# edited by Zhu Wenyuan


import json
from datetime import datetime
from validation import validate_task_list
def is_valid_date(s):
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False

def validate_task(task: dict):
    """Check the specification of a single task field"""
    required_keys = {"id", "title", "priority", "completed", "due_date", "tags"}
    if not required_keys.issubset(task.keys()):
        return False, f"Task{task.get('id')} is missing required keys, the current tasks will not be changed"
    if not isinstance(task["id"], int) or task["id"] <= 0:
        return False, f"Task{task.get('id')} is not a positive integer, the current tasks will not be changed"
    if not isinstance(task["title"], str):
        return False, f"Task{task.get('id')} is not a string, the current tasks will not be changed"
    if task["priority"] not in ["Low", "Medium", "High"]:
        return False, f"Task{task.get('id')} is not a valid priority, the current tasks will not be changed"
    if not isinstance(task["completed"], bool):
        return False, f"Task{task.get('id')} is not a boolean, the current tasks will not be changed"
    if not is_valid_date(task["due_date"]):
        return False, f"Task{task.get('id')} is not a valid date, the current tasks will not be changed"
    if not isinstance(task["tags"], list):
        return False, f"Task{task.get('id')} is not a list, the current tasks will not be changed"

    return True, ""





def load_tasks(file_path="tasks.json"):
    """Load data before the start of the main program flow, and read existing data from tasks.json"""

    print("The tasks is loading....")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tasks = json.load(f)
            print("Tasks are successfully loaded")
            return tasks
    except FileNotFoundError:
        print("tasks.json file not found")
        return None
    except Exception as e:
        print(f"Failed to load tasks, error: {e}")
        return None

def save_tasks(tasks, file_path="tasks.json"):
    """Save the data. The saving operation can be performed during program execution or when the program is about to terminate."""

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            print("The tasks is saving....")
            saving_tasks = []
            for n in tasks:
                saving_tasks.append(n)
            f.write(json.dumps(saving_tasks, ensure_ascii=False, indent=4))
        print("Tasks are successfully saved")
        return True
    except:
        print("Failed to save tasks")
        return False

def import_tasks(current_task, file_path):
    """Import the tasks from the other file path."""
    print("The tasks is importing....")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tasks_imported = json.load(f)
            print("Imported tasks are successfully loaded")

    except FileNotFoundError:
        print(f"{file_path} file not found, the current tasks will not be changed")
        return current_task
    except json.decoder.JSONDecodeError:
        print(f"{file_path} is not valid json, the current tasks will not be changed")
        return current_task
    except Exception as e:
        print(f"Failed to load tasks, error: {e}, the current tasks will not be changed")
        return current_task
    if not isinstance(tasks_imported, list):
        print("Imported file must be a list of tasks, current tasks unchanged")
        return current_task
    try:
        tasks_imported = validate_task_list(tasks_imported)
    except ValueError as e:
        print(f"Invalid imported tasks: {e}. Current tasks unchanged.")
        return current_task
    print("Do you want to use the imported tasks to replace the current tasks?(not saved yet) Please enter [Yes] or [No]")
    while True:
        choice = input().lower()
        if choice == "yes":
            print("Tasks are successfully imported")
            return tasks_imported
        elif choice == "no":
            return current_task
        else:
            print("Please enter valid option")














