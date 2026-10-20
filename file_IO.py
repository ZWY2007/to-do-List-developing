# edited by Zhu Wenyuan

import json


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






