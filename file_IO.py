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
    """检验单个task字段规范"""
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
    """主程序流程开始前对数据进行加载，从tasks.json中读取现有数据"""

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
    """对数据进行保存，可以在程序执行中或程序即将终止时执行保存操作"""
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
    """用户从其他文件路径导入任务， task_1参数需输入当前任务库，file_path参数为用户输入文件路径， 函数中请求全局变量tasks，若导入文件合规，则给当前全局变量tasks赋值导入的
    tasks_imported"""
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














