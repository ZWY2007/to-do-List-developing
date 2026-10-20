"""Optional task-processing functions implemented by team member 4.

All functions in this module are pure data-processing functions:
- they do not call input() or print();
- they do not modify the original tasks list;
- they use the function names and parameters defined in interface.txt.
"""


def filter_tasks(tasks, filter_type, condition):
    """Return tasks matching the specified condition.

    Supported filter types:
        "id"        - match a task ID
        "title"     - match a title (case-insensitive)
        "priority"  - match High, Medium, or Low (case-insensitive)
        "completed" - match True or False
        "due_date"  - match a YYYY-MM-DD string or None
        "tags"      - include tasks containing the specified tag

    The original tasks list is not modified.
    """
    supported_types = {
        "id", "title", "priority", "completed", "due_date", "tags"
    }

    if not isinstance(filter_type, str):
        raise ValueError("filter_type must be a string")

    normalized_type = filter_type.strip().lower()
    if normalized_type not in supported_types:
        raise ValueError(f"Unsupported filter type: {filter_type}")

    if normalized_type == "tags":
        if not isinstance(condition, str):
            raise ValueError("The tag condition must be a string")
        wanted_tag = condition.strip().casefold()
        return [
            task
            for task in tasks
            if any(
                str(tag).strip().casefold() == wanted_tag
                for tag in task.get("tags", [])
            )
        ]

    if normalized_type in {"title", "priority"}:
        if not isinstance(condition, str):
            raise ValueError(f"The {normalized_type} condition must be a string")
        wanted_value = condition.strip().casefold()
        return [
            task
            for task in tasks
            if isinstance(task.get(normalized_type), str)
            and task[normalized_type].strip().casefold() == wanted_value
        ]

    if normalized_type == "completed" and not isinstance(condition, bool):
        raise ValueError("The completed condition must be True or False")

    return [
        task for task in tasks if task.get(normalized_type) == condition
    ]


def sort_tasks(tasks, sort_type):
    """Return a sorted copy of tasks without changing the original list.

    Supported sort types:
        "id"        - ascending numeric ID
        "title"     - alphabetical title order
        "priority"  - High, Medium, then Low
        "completed" - uncompleted tasks, then completed tasks
        "due_date"  - earliest date first; tasks without a date go last
    """
    if not isinstance(sort_type, str):
        raise ValueError("sort_type must be a string")

    normalized_type = sort_type.strip().lower()
    priority_order = {"high": 0, "medium": 1, "low": 2}

    if normalized_type == "id":
        return sorted(tasks, key=lambda task: int(task["id"]))

    if normalized_type == "title":
        return sorted(tasks, key=lambda task: task["title"].casefold())

    if normalized_type == "priority":
        return sorted(
            tasks,
            key=lambda task: priority_order[task["priority"].casefold()],
        )

    if normalized_type == "completed":
        return sorted(tasks, key=lambda task: task["completed"])

    if normalized_type == "due_date":
        return sorted(
            tasks,
            key=lambda task: (
                task.get("due_date") is None,
                task.get("due_date") or "",
            ),
        )

    raise ValueError(f"Unsupported sort type: {sort_type}")


def get_statistics(tasks):
    """Return total, completion counts, and completion percentage.

    completion_rate is a percentage from 0.0 to 100.0. For an empty task
    list, completion_rate is 0.0.
    """
    total = len(tasks)
    completed = sum(task.get("completed") is True for task in tasks)
    uncompleted = total - completed
    completion_rate = round(completed / total * 100, 2) if total else 0.0

    return {
        "total": total,
        "completed": completed,
        "uncompleted": uncompleted,
        "completion_rate": completion_rate,
    }
