"""Core task operations for the To-Do List project (Member 2).

This module follows interface.txt. It never reads input, prints output,
or accesses files. Operations modify the given tasks list in place.
"""

from datetime import date


PRIORITIES = ("High", "Medium", "Low")


def _valid_id(value):
    """Return True for a positive integer ID (but not a Boolean)."""
    return type(value) is int and value > 0


def _find_task(tasks, task_id):
    """Find one task by its unique ID; return None if not found."""
    if not isinstance(tasks, list) or not _valid_id(task_id):
        return None
    for task in tasks:
        if isinstance(task, dict) and task.get("id") == task_id:
            return task
    return None


def _valid_title(value):
    return isinstance(value, str) and bool(value.strip())


def _valid_priority(value):
    return value in PRIORITIES


def _valid_due_date(value):
    if value is None:
        return True
    if not isinstance(value, str):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def _valid_tags(value):
    return isinstance(value, list) and all(
        isinstance(tag, str) and bool(tag.strip()) for tag in value
    )


def add_task(tasks, title, priority, due_date=None, tags=None):
    """Append a new task; return its dict, or None for invalid data.

    ID is max(existing integer IDs) + 1, or 1 if tasks is empty.
    All existing tasks must use valid, unique positive integer IDs.
    """
    if not isinstance(tasks, list):
        return None
    if not (_valid_title(title) and _valid_priority(priority)
            and _valid_due_date(due_date)):
        return None
    if tags is None:
        tags = []
    if not _valid_tags(tags):
        return None

    ids = []
    for task in tasks:
        if not isinstance(task, dict) or not _valid_id(task.get("id")):
            return None
        ids.append(task["id"])
    if len(ids) != len(set(ids)):
        return None

    new_task = {
        "id": max(ids, default=0) + 1,
        "title": title.strip(),
        "priority": priority,
        "completed": False,
        "due_date": due_date,
        "tags": tags.copy(),
    }
    tasks.append(new_task)
    return new_task


def modify_task(tasks, task_id, new_info):
    """Update only fields listed in new_info; return success Boolean.

    Editable fields: title, priority, due_date, tags.
    Use toggle_completed for status; ID cannot be edited.
    Validate all fields BEFORE changing the task.
    """
    task = _find_task(tasks, task_id)
    if task is None or not isinstance(new_info, dict) or not new_info:
        return False

    allowed = {"title", "priority", "due_date", "tags"}
    if not set(new_info).issubset(allowed):
        return False

    updates = {}
    for key, value in new_info.items():
        if key == "title":
            if not _valid_title(value):
                return False
            updates[key] = value.strip()
        elif key == "priority":
            if not _valid_priority(value):
                return False
            updates[key] = value
        elif key == "due_date":
            if not _valid_due_date(value):
                return False
            updates[key] = value
        elif key == "tags":
            if not _valid_tags(value):
                return False
            updates[key] = value.copy()

    task.update(updates)
    return True


def delete_task(tasks, task_id):
    """Remove a task by ID; return True if removed, else False."""
    task = _find_task(tasks, task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True


def toggle_completed(tasks, task_id):
    """Reverse the completed Boolean for one task; return success."""
    task = _find_task(tasks, task_id)
    if task is None or type(task.get("completed")) is not bool:
        return False
    task["completed"] = not task["completed"]
    return True


def set_priority(tasks, task_id, new_priority):
    """Set priority to High, Medium or Low; return success."""
    task = _find_task(tasks, task_id)
    if task is None or not _valid_priority(new_priority):
        return False
    task["priority"] = new_priority
    return True
