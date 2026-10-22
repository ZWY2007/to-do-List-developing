from task_operations import add_task, modify_task, delete_task, toggle_completed, set_priority
from optional_functions import filter_tasks, sort_tasks, get_statistics
from file_IO import load_tasks, save_tasks, import_tasks
from validation import validate_title, validate_task_id, validate_due_date, validate_priority, validate_tags, validate_menu_choice 

def welcome_message(): # print the welcome message
    print("Welcome to the Task Management System!")
    print("Manage your tasks efficiently and effectively.")

def show_menu(): # print the menu options,return the user input
    print("======== Function Menu ========")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Modify task")
    print("4. Delete task")
    print("5. Mark task complete/incomplete")
    print("6. Set task priority")
    print("7. Filter tasks")
    print("8. Sort tasks")
    print("9. Task statistics")
    print("10. Save tasks to file")
    print("11. Load tasks from file")
    print("0. Exit")
    choice = input("Please enter option number: ")
    try:
        choice = validate_menu_choice(choice)
    except ValueError as e:
        print(e)
        return None
    return choice

def show_filter_submenu(): # print the filter submenu options,return the user input
    print("======== Filter Submenu ========")
    print("1. Filter by completion status")
    print("2. Filter by priority")
    print("3. Filter by due date")
    print("4. Filter by tag")
    print("0. Back to main menu")
    choice = input("Please enter option number: ")
    try:
        choice = validate_menu_choice(choice)
    except ValueError as e:
        print(e)
        return None
    return choice

def show_sort_submenu(): # print the sort submenu options,return the user input
    print("======== Sort Submenu ========")
    print("1. Sort by priority (high-medium-low)")
    print("2. Sort by due date")
    print("3. Sort by task ID")
    print("0. Back to main menu")
    choice = input("Please enter option number: ")
    try:
        choice = validate_menu_choice(choice)
    except ValueError as e:
        print(e)
        return None
    return choice

def view_all_tasks(tasks): # print all tasks in a formatted way
    if not tasks:
        print("No tasks available.")
        return
    print("======== All Tasks ========")
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, Completed: {task['completed']}, Due Date: {task['due_date']}, Tags: {', '.join(task['tags'])}")


def main():  # main loop of the program, handle user input and call corresponding functions
    tasks = load_tasks()
    if tasks is None:
        print("Failed to load task file.")
        choice = input("Do you want to continue with an empty task list?(y/n): ")
        if choice.lower() == "y":
            tasks = []
            has_change = False
        else:
            print("Program exit.")
            return
    else:
        has_change = False
    welcome_message()
    while True:
        opt = show_menu()
        
        if opt == "1":
            # Add task
            print("--- Add Task ---")
            title = input("Task title: ").strip()
            if not validate_title(title):
                print("Invalid task title.")
                continue
            priority = input("Priority (High/Medium/Low): ")
            if not validate_priority(priority):
                print("Invalid priority.")
                continue
            due_date = input("Due date(YYYY-MM-DD): ").strip()
            if not validate_due_date(due_date):
                print("Invalid due date.")
                continue
            # 空输入转为None
            if due_date == "":
                due_date = None
            tags = input("Tags(space-separated): ").split()
            if not validate_tags(tags):
                print("Invalid tags.")
                continue
            success = add_task(tasks, title, priority, due_date, tags)
            if success:
                print("Task added successfully.")
                has_change = True

        elif opt == "2":
            # View all tasks
            print("--- All Tasks ---")
            view_all_tasks(tasks)

        elif opt == "3":
            # Modify task
            print("--- Modify Task ---")
            try:
                tid = int(input("Enter task ID to modify: "))
            except ValueError:
                print("Error: Task ID must be integer!")
                continue
            if not validate_task_id(tasks, tid):
                print(f"Task with id {tid} does not exist.")
                continue
            new_info = {}
            fields = [
                ("title", "New title (enter to skip): "),
                ("priority", "New priority (enter to skip): "),
            ]
            for k, prompt in fields:
                val = input(prompt).strip()
                if val:
                    if k == "title":
                        if not validate_title(val):
                            print("Invalid title.")
                            continue
                    if k == "priority":
                        if not validate_priority(val):
                            print("Invalid priority.")
                            continue
                    new_info[k] = val
            # due_date特殊处理,无论是否为空，都要传入payload，None表示空
            due_val = input("New due date (YYYY-MM-DD, enter to skip): ").strip()
            if due_val:
                if not validate_due_date(due_val):
                    print("Invalid due date.")
                    continue
                new_info["due_date"] = due_val
            tags = input("New tags (space split, enter to skip): ").split()
            if not validate_tags(tags):
                print("Invalid tags.")
                continue
            if tags:
                new_info["tags"] = tags
            success = modify_task(tasks, tid, new_info)
            if success:
                print("Task modified successfully.")
                has_change = True
            else:
                print("Failed to modify task.")

        elif opt == "4":
            # Delete task
            print("--- Delete Task ---")
            try:
                tid = int(input("Enter task ID to delete: "))
            except ValueError:
                print("Error: Task ID must be integer!")
                continue
            if not validate_task_id(tasks, tid):
                print(f"Task with id {tid} does not exist.")
                continue
            # 先查找任务
            found_task = None
            for t in tasks:
                if t["id"] == tid:
                    found_task = t
                    break
            if found_task is None:
                print(f"Task with id {tid} does not exist.")
                continue
            # 展示任务信息 + 用户确认
            print("\nTask information to delete:")
            print(f"ID: {found_task['id']}")
            print(f"Title: {found_task['title']}")
            print(f"Priority: {found_task['priority']}")
            print(f"Completed: {found_task['completed']}")
            print(f"Due date: {found_task['due_date']}")
            print(f"Tags: {found_task['tags']}")
            confirm = input("\nAre you sure you want to DELETE this task? [Yes/No]: ").lower()
            if confirm != "yes":
                print("Delete cancelled.")
                continue
            success = delete_task(tasks, tid)
            if success:
                print("Task deleted successfully.")
                has_change = True

        elif opt == "5":
            # Toggle completed status
            print("--- Toggle Task Completion ---")
            try:
                tid = int(input("Enter task ID: "))
            except ValueError:
                print("Error: Task ID must be integer!")
                continue
            if not validate_task_id(tasks, tid):
                print(f"Task with id {tid} does not exist.")
                continue
            success = toggle_completed(tasks, tid)
            if success:
                print("Task completion status toggled.")
                has_change = True

        elif opt == "6":
            # Set priority
            print("--- Set Task Priority ---")
            try:
                tid = int(input("Enter task ID: "))
            except ValueError:
                print("Error: Task ID must be integer!")
                continue
            if not validate_task_id(tasks, tid):
                print(f"Task with id {tid} does not exist.")
                continue
            new_p = input("Set priority (High/Medium/Low): ")
            success = set_priority(tasks, tid, new_p)
            if success:
                print("Task priority set successfully.")
                has_change = True

        elif opt == "7":
            # Filter tasks，调用子菜单
            print("--- Filter Tasks ---")
            sub_opt = show_filter_submenu()
            if sub_opt == "0":
                print("Back to main menu.")
                continue
            arg = input("Filter value: ")
            if sub_opt == "1":  # sub_opt=1：按完成状态筛选
                if arg.lower() in ["true", "yes", "1"]:
                    arg = True   # 字符串 → 布尔True
                elif arg.lower() in ["false", "no", "0"]:
                    arg = False  # 字符串 → 布尔False
            filtered_list = filter_tasks(tasks, sub_opt, arg)
            view_all_tasks(filtered_list)

        elif opt == "8":
            # Sort tasks，调用子菜单
            print("--- Sort Tasks ---")
            sort_sub_opt = show_sort_submenu()
            if sort_sub_opt == "0":
                print("Back to main menu.")
                continue
            sorted_list = sort_tasks(tasks, sort_sub_opt)
            view_all_tasks(sorted_list)

        elif opt == "9":
            # Statistics
            print("--- Task Statistics ---")
            stats = get_statistics(tasks)
            print(f"Total:{stats['total']}, Completed:{stats['completed']}, Incomplete:{stats['uncompleted']}, Rate:{stats['completion_rate']:.1f}%")

        elif opt == "10":
            # Save manually
            print("--- Save Tasks ---")
            save_success = save_tasks(tasks)
            if save_success:
                has_change = False
                print("Save successfully.")
            else:
                print("Save failed! The unsaved changes are retained.")

        elif opt == "11":
            # Import tasks
            print("--- Import Tasks ---")
            file_path = input("Input file path: ")
            # 接收函数返回的tasks列表
            new_tasks = import_tasks(tasks, file_path)
            if new_tasks is not tasks:
                tasks = new_tasks
                has_change = True

        elif opt == "0":
            # Exit
            if has_change:
                print("You have unsaved changes!")
                print("(1) Save and Exit")
                print("(2) Exit without Saving")
                print("(3) Cancel, back to menu")
                ex_choice = input("Please choose 1/2/3: ")
                if ex_choice == "1":
                    save_success = save_tasks(tasks)
                    if save_success:
                        print("Saved. Program exit.")
                    else:
                        print("Save failed! Cannot save, return to menu.")
                        continue
                    break
                elif ex_choice == "2":
                    print("Discard changes. Program exit.")
                    break
                elif ex_choice == "3":
                    print("Exit cancelled, return main menu.")
                    continue
                else:
                    print("Invalid choice, back to menu.")
                    continue
            else:
                print("No unsaved changes, program exit.")
                break
        else:
            print("Invalid input! Please input number from 0-11.")

if __name__ == "__main__":
    main()
