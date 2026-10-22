from datetime import datetime


def validate_title(value):
    """Check that a task title is not empty."""

    if not isinstance(value, str) or not value.strip():
        raise ValueError("Task title cannot be empty.")

    return value.strip()


def validate_task_id(value):
    """Check that a task ID is a positive integer."""

    if isinstance(value, bool):
        raise ValueError("Task ID must be a positive integer.")

    if isinstance(value, int):
        task_id = value

    elif isinstance(value, str):
        value = value.strip()

        if not value.isdecimal():
            raise ValueError("Task ID must be a positive integer.")

        task_id = int(value)

    else:
        raise ValueError("Task ID must be a positive integer.")

    if task_id <= 0:
        raise ValueError("Task ID must be a positive integer.")

    return task_id


def validate_priority(value):
    """Return High, Medium, or Low."""

    if not isinstance(value, str):
        raise ValueError("Priority must be High, Medium, or Low.")

    priority = value.strip().lower()

    if priority == "high":
        return "High"
    elif priority == "medium":
        return "Medium"
    elif priority == "low":
        return "Low"
    else:
        raise ValueError("Priority must be High, Medium, or Low.")


def validate_due_date(value):
    """Check the date format YYYY-MM-DD, or return None."""

    if value is None:
        return None

    if not isinstance(value, str):
        raise ValueError("Due date must be YYYY-MM-DD.")

    due_date = value.strip()

    # The user can leave the due date empty.
    if due_date == "":
        return None

    # Check that the format has 10 characters: YYYY-MM-DD.
    if len(due_date) != 10:
        raise ValueError("Due date must be YYYY-MM-DD.")

    if due_date[4] != "-" or due_date[7] != "-":
        raise ValueError("Due date must be YYYY-MM-DD.")

    # Check that the date really exists, such as February 28 vs 30.
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date is not valid.")

    return due_date


def validate_tags(value):
    """Return a list of tag strings."""

    if value is None:
        return []

    # The CLI may use a string with spaces between tags.
    if isinstance(value, str):
        value = value.split()

    if not isinstance(value, list):
        raise ValueError("Tags must be a list or a string.")

    tags = []

    for tag in value:
        if not isinstance(tag, str):
            raise ValueError("Each tag must be a string.")

        tag = tag.strip()
        if tag == "":
            raise ValueError("Tags cannot be empty strings.")

        tags.append(tag)

    return tags


def validate_menu_choice(value):
    """Check the main menu choice (0 to 11)."""

    if not isinstance(value, str):
        raise ValueError("Invalid menu choice.")

    choice = value.strip()
    choices = ["0", "1", "2", "3", "4", "5", "6", "7",
               "8", "9", "10", "11"]

    if choice not in choices:
        raise ValueError("Invalid menu choice.")

    return choice
