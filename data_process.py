import json

class Data_Process:

    def __init__(self, tasks: list | None = None):
        if tasks is None:
            self.tasks = []
        else:
            self.tasks = tasks

    def check_all_tasks(self):
        """用于查看全部任务"""
        task_list = []
        for all_tasks in self.tasks:
            task_list.append(all_tasks)
        return task_list

    def sorted_tasks(self, sorted_type):
        """用于给任务排序"""
        pass

    def choose_tasks(self):
        """用于筛选任务"""
        pass

    def append_tasks(self, id, title, priority, completed, due_date, tags):
        """用于添加任务"""
        pass

    def modify_tasks(self, id, title, priority, completed, due_date, tags):
        """用于修改任务"""
        pass

    def delete_tasks(self, id):
        """用于删除任务"""
        pass

    def edit_tasks(self, id, completed: bool, priority):
        """用于标记任务是否完成，设置任务优先级等"""
        pass

    def analyse_tasks(self):
        """用于统计任务"""
        pass

    def save_tasks(self, file_path="tasks.json"):
        """保存进默认json文件或其他文件"""
        pass
    def __iter__(self):
        return iter(self.tasks)








