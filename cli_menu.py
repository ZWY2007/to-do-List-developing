from task_operations import add_task, modify_task, delete_task, toggle_completed, set_priority
from  import filter_tasks, sort_tasks, get_statistics
from file_IO import load_tasks, save_tasks, import_tasks

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
    return choice

def show_filter_submenu(): # print the filter submenu options,return the user input
    print("======== Filter Submenu ========")
    print("1. Filter by completion status")
    print("2. Filter by priority")
    print("3. Filter by due date")
    print("4. Filter by tag")
    print("0. Back to main menu")
    choice = input("Please enter option number: ")
    return choice

def show_sort_submenu(): # print the sort submenu options,return the user input
    print("======== Sort Submenu ========")
    print("1. Sort by priority (high-medium-low)")
    print("2. Sort by due date")
    print("3. Sort by task ID")
    print("0. Back to main menu")
    choice = input("Please enter option number: ")
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
    has_change = False
    welcome_message()
    while True:
        opt = show_menu()
        if opt == "1":
            # Add task
            print("--- Add Task ---")
            title = input("Task title: ")
            priority = input("Priority (High/Medium/Low): ")
            due_date = input("Due date(YYYY-MM-DD): ")
            tags = input("Tags(space-separated): ").split()
            add_task(tasks, title, priority, due_date, tags)
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
            title = input("New title (enter to skip): ")
            prio = input("New priority (enter to skip): ")
            dued = input("New due date (enter to skip): ")
            tags_in = input("New tags (space split, enter to skip): ").split()
            modify_task(tasks, tid, title, prio, dued, tags_in)
            has_change = True

        elif opt == "4":
            # Delete task
            print("--- Delete Task ---")
            try:
                tid = int(input("Enter task ID to delete: "))
            except ValueError:
                print("Error: Task ID must be integer!")
                continue
            delete_task(tasks, tid)
            has_change = True

        elif opt == "5":
            # Toggle completed status
            print("--- Toggle Task Completion ---")
            try:
                tid = int(input("Enter task ID: "))
            except ValueError:
                print("Error: Task ID must be integer!")
                continue
            toggle_completed(tasks, tid)
            has_change = True

        elif opt == "6":
            # Set priority
            print("--- Set Task Priority ---")
            try:
                tid = int(input("Enter task ID: "))
            except ValueError:
                print("Error: Task ID must be integer!")
                continue
            new_p = input("Set priority (High/Medium/Low): ")
            set_priority(tasks, tid, new_p)
            has_change = True

        elif opt == "7":
            # Filter tasks，调用子菜单
            print("--- Filter Tasks ---")
            sub_opt = show_filter_submenu()
            if sub_opt == "0":
                print("Back to main menu.")
                continue
            arg = input("Filter value: ")
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
            total, finished, unfinished, rate = get_statistics(tasks)
            print(f"Total:{total}, Completed:{finished}, Incomplete:{unfinished}, Rate:{rate:.1f}%")

        elif opt == "10":
            # Save manually
            print("--- Save Tasks ---")
            save_tasks(tasks)
            has_change = False

        elif opt == "11":
            # Import tasks
            print("--- Import Tasks ---")
            file_path = input("Input file path: ")
            import_tasks(tasks, file_path)
            has_change = True

        elif opt == "0":
            # Exit with 3 options
            if has_change:
                print("You have unsaved changes!")
                print("(1) Save and Exit")
                print("(2) Exit without Saving")
                print("(3) Cancel, back to menu")
                ex_choice = input("Please choose 1/2/3: ")
                if ex_choice == "1":
                    save_tasks(tasks)
                    print("Saved. Program exit.")
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
