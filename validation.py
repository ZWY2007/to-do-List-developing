from datetime import datetime


def validate_title(value):
    """Return a non-empty title without surrounding spaces."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Task title cannot be empty.")
    return value.strip()


def validate_task_id(value):
    """Return a positive numeric STRING ID, such as '01' or '02'.

    '1' and '01' refer to the same ID in Member 2's task_operations.py.
    The CLI may pass a string or an integer; the return value is always str.
    """
    if isinstance(value, bool):
        raise ValueError("Task ID must be a positive numeric string.")

    if isinstance(value, int):
        number = value
    elif isinstance(value, str):
        value = value.strip()
        if not value or not value.isascii() or not value.isdecimal():
            raise ValueError("Task ID must be a positive numeric string.")
        number = int(value)
    else:
        raise ValueError("Task ID must be a positive numeric string.")

    if number <= 0:
        raise ValueError("Task ID must be a positive numeric string.")
    return f"{number:02d}"


def validate_priority(value):
    """Return exactly 'High', 'Medium', or 'Low'."""
    if not isinstance(value, str):
        raise ValueError("Priority must be High, Medium, or Low.")
    priority = value.strip().lower()
    if priority == "high":
        return "High"
    if priority == "medium":
        return "Medium"
    if priority == "low":
        return "Low"
    raise ValueError("Priority must be High, Medium, or Low.")


def validate_due_date(value):
    """Return a YYYY-MM-DD date, or None for an optional blank date."""
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError("Due date must be YYYY-MM-DD.")
    due_date = value.strip()
    if not due_date:
        return None
    if len(due_date) != 10 or due_date[4] != "-" or due_date[7] != "-":
        raise ValueError("Due date must be YYYY-MM-DD.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date is not valid.")
    return due_date


def validate_tags(value):
    """Return a list of non-empty strings, or [] for no tags."""
    if value is None:
        return []
    if isinstance(value, str):
        value = value.split()
    if not isinstance(value, list):
        raise ValueError("Tags must be a list or a string.")
    tags = []
    for tag in value:
        if not isinstance(tag, str) or not tag.strip():
            raise ValueError("Each tag must be a non-empty string.")
        tags.append(tag.strip())
    return tags


def validate_menu_choice(value, allowed_choices=None):
    """Check menu input: default 0-11; pass choices for a submenu."""
    if not isinstance(value, str):
        raise ValueError("Invalid menu choice.")
    choice = value.strip()
    if allowed_choices is None:
        allowed_choices = [str(number) for number in range(12)]
    if choice not in allowed_choices:
        raise ValueError("Invalid menu choice.")
    return choice


def validate_completed_filter(value):
    """Convert a completed-status filter into a real Boolean."""
    if isinstance(value, bool):
        return value
    if not isinstance(value, str):
        raise ValueError("Completed filter must be yes/no or true/false.")
    answer = value.strip().lower()
    if answer in ["yes", "y", "true", "1"]:
        return True
    if answer in ["no", "n", "false", "0"]:
        return False
    raise ValueError("Completed filter must be yes/no or true/false.")


def validate_task_list(value):
    """Check imported/saved task data without changing it.

    Return a clean new list if every task is valid. Reject duplicate IDs,
    including IDs such as '1' and '01' which refer to the same task.
    """
    if not isinstance(value, list):
        raise ValueError("Tasks must be a list.")

    required = {"id", "title", "priority", "completed", "due_date", "tags"}
    seen_ids = set()
    cleaned = []

    for task in value:
        if not isinstance(task, dict) or not required.issubset(task):
            raise ValueError("Each task must have all required fields.")

        # Imported IDs must already be strings, as required by Member 2.
        if not isinstance(task["id"], str):
            raise ValueError("Imported task IDs must be strings.")
        task_id = validate_task_id(task["id"])
        if task_id in seen_ids:
            raise ValueError("Duplicate task ID found.")
        seen_ids.add(task_id)
        if not isinstance(task["completed"], bool):
            raise ValueError("Task completed must be True or False.")
        if task["priority"] not in ["High", "Medium", "Low"]:
            raise ValueError("Imported priority must be High, Medium, or Low.")
        if not isinstance(task["tags"], list):
            raise ValueError("Imported tags must be a list.")

        new_task = dict(task)
        new_task["id"] = task_id
        new_task["title"] = validate_title(task["title"])
        new_task["due_date"] = validate_due_date(task["due_date"])
        new_task["tags"] = validate_tags(task["tags"])
        cleaned.append(new_task)

    return cleaned
