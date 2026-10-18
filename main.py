from data_process import Data_Process
import json


with open("tasks.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)


if __name__ == '__main__':
    data = Data_Process(tasks)
    print(data.check_all_tasks())