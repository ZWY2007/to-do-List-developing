# edited by Zhu Wenyuan

import json
from datetime import datetime
def is_valid_date(s):
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except ValueError:
        return False
def load_tasks(file_path="tasks.json"):
    """主程序流程开始前对数据进行加载，从tasks.json中读取现有数据"""

    print("The tasks is loading....")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tasks = json.load(f)
            print("Tasks are successfully loaded")
            return tasks
    except FileNotFoundError:
        print("tasks.json file not found, use empty task list")
        tasks = []
        return tasks
    except Exception as e:
        print(f"Failed to load tasks, error: {e}")
        tasks = []
        return tasks

def save_tasks(tasks, file_path="tasks.json"):
    """对数据进行保存，可以在程序执行中或程序即将终止时执行保存操作"""
    with open(file_path, "w", encoding="utf-8") as f:
        print("The tasks is saving....")
        saving_tasks = []
        for n in tasks:
            saving_tasks.append(n)
        f.write(json.dumps(saving_tasks, ensure_ascii=False, indent=4))
    print("Tasks are successfully saved")
    return True

def import_tasks(tasks_1, file_path):
    """用户从其他文件路径导入任务"""
    print("The tasks is importing....")
    global tasks
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tasks_imported = json.load(f)
            print(" Imported tasks are successfully loaded")

    except FileNotFoundError:
        print(f"{file_path} file not found, the current tasks will not be changed")
        return tasks_1

    except Exception as e:
        print(f"Failed to load tasks, error: {e}, the current tasks will not be changed")
        return tasks_1
    required_keys = {"id", "title", "priority", "completed", "due_date", "tags"}
    for n in tasks_imported:
        if not required_keys.issubset(n.keys()):
            print(f"{n} is missing required keys, the current tasks will not be changed")
            return tasks_1
        if not isinstance(n["id"], str):
            print(f"{n} is not a string, the current tasks will not be changed")
            return tasks_1
        if not isinstance(n["title"], str):
            print(f"{n} is not a string, the current tasks will not be changed")
            return tasks_1
        if n["priority"] not in ["Low", "Medium", "High"]:
            print(f"{n} is not a valid priority, the current tasks will not be changed")
            return tasks_1
        if not isinstance(n["completed"], bool):
            print(f"{n} is not a boolean, the current tasks will not be changed")
            return tasks_1
        if not is_valid_date(n["due_date"]):
            print(f"{n} is not a valid date, the current tasks will not be changed")
        if not isinstance(n["tags"], list):
            print(f"{n} is not a list, the current tasks will not be changed")
            return tasks_1
    print("Do you want to use the imported tasks to replace the current tasks?(not saved yet) Please enter [Yes] or [No]")
    while True:
        choice = input().lower()
        if choice == "yes":
            tasks = tasks_imported
            print("Tasks are successfully imported")
            return tasks
        elif choice == "no":
            return tasks_1
        else:
            print("Please enter valid option")













