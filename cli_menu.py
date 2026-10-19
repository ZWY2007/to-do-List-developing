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
