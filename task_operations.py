"""Core task operations for the To-Do List project (Member 2).

This module uses STRING task IDs (e.g. "01", "02") exclusively.
It never reads input, prints output,
or accesses files. Operations modify the given tasks list in place.
"""

from datetime import date


PRIORITIES = ("High", "Medium", "Low")


def _normalise_id(value):
    """Validate a STRING ID and return its numeric value for comparison.

    All stored IDs and task_id arguments must be strings.  "1" and "01"
    represent the same task ID; integer 1 is not accepted.
    """
    if not isinstance(value, str) or not value.isascii() or not value.isdecimal():
        return None
    numeric_id = int(value)
    return numeric_id if numeric_id > 0 else None


def _valid_id(value):
    """Return True for a positive numeric string ID, never for an integer."""
    return _normalise_id(value) is not None


def _find_task(tasks, task_id):
    """Find a task using a string ID; return None if not found."""
    target = _normalise_id(task_id)
    if not isinstance(tasks, list) or target is None:
        return None
    for task in tasks:
        if isinstance(task, dict) and _normalise_id(task.get("id")) == target:
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

    IDs are numeric STRINGS: "01", "02", "03", ...
    All existing tasks must have unique, positive numeric-string IDs.
    The new ID is max(existing numeric IDs) + 1, formatted as a string.
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
        ids.append(_normalise_id(task["id"]))
    if len(ids) != len(set(ids)):
        return None

    next_id = max(ids, default=0) + 1
    new_task = {
        "id": f"{next_id:02d}",
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
