
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
