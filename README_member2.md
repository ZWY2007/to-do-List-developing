# Member 2 - Essential Task Functions

## Contents

- `task_operations.py`: the five pure-data functions from `interface.txt`.
- `test_task_operations.py`: unit tests for successful and unsuccessful operations.

## Integration into team project

Copy `task_operations.py` into the repository root, alongside `main.py`.
Other members can import your functions:

```python
from task_operations import add_task, modify_task, delete_task, toggle_completed, set_priority
```

All five functions mutate the supplied `tasks` list **in place**. They never use `input()`, `print()`, or file I/O.

| Function | Return on success | Return on failure |
| --- | --- | --- |
| `add_task(tasks, title, priority, due_date=None, tags=None)` | new task dict | `None` |
| `modify_task(tasks, task_id, new_info)` | `True` | `False` |
| `delete_task(tasks, task_id)` | `True` | `False` |
| `toggle_completed(tasks, task_id)` | `True` | `False` |
| `set_priority(tasks, task_id, new_priority)` | `True` | `False` |

`modify_task` takes a partial dictionary, e.g. `{"title": "New title"}`. Supported keys: `title`, `priority`, `due_date`, `tags`. To change completion status, call `toggle_completed` instead. IDs cannot be modified.

### Important preconditions

- **Data issue in original `tasks.json`:** IDs are strings like `"01"`, `"02"` and one priority is `"low"`. Team should normalize those to integer `1`, `2` and canonical `"Low"` before using these functions. This code intentionally does not silently convert malformed loaded data.
- The agreed priorities are **exactly** `High`, `Medium`, `Low`. Member 5's `validate_priority` should normalize user input before calls.
- Dates must be `YYYY-MM-DD` or `None`; tags must be lists of non-empty strings.
- ID generation uses `max(existing IDs) + 1` (or 1 for an empty list). This does **not** guarantee that a deleted ID is never reused; the current interface only guarantees uniqueness among existing tasks. Discuss using a persisted `next_id` if permanent uniqueness is required.
- `Data_Process` in the old `data_process.py` is a different interface. The agreed `interface.txt` calls for standalone functions, so Member 3 should import these standalone functions into the CLI and should not assume the old class methods call them automatically.

## Run unit tests

From the directory containing these two `.py` files:

```bash
python -m unittest test_task_operations.py -v
```

No changes to `main.py`, `tasks.json`, or other member's code are included here.
