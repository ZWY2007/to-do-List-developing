from validation import (
    validate_title, validate_task_id, validate_priority, validate_due_date,
    validate_tags, validate_menu_choice, validate_completed_filter,
    validate_task_list,
)


def must_reject(function, value, *args):
    try:
        function(value, *args)
    except ValueError:
        return
    raise AssertionError(f"Invalid value was accepted: {function.__name__}({value!r})")


# 1. Title
assert validate_title("  Finish homework  ") == "Finish homework"
for bad in ["", "   ", None, 123]:
    must_reject(validate_title, bad)
print("Test 1 passed: title")

# 2. IDs must work with Member 2's string-ID code
assert validate_task_id("1") == "01"
assert validate_task_id("01") == "01"
assert validate_task_id(" 2 ") == "02"
assert validate_task_id(3) == "03"
assert validate_task_id("100") == "100"
for bad in ["abc", "0", "-2", "", None, True, 1.5, "1.0", "１２"]:
    must_reject(validate_task_id, bad)
print("Test 2 passed: string task ID")

# 3. Priority
assert validate_priority(" HIGH ") == "High"
assert validate_priority("MEDIUM") == "Medium"
assert validate_priority("low") == "Low"
for bad in ["Urgent", "", None, 123]:
    must_reject(validate_priority, bad)
print("Test 3 passed: priority")

# 4. Optional date
assert validate_due_date("2026-10-22") == "2026-10-22"
assert validate_due_date("") is None
assert validate_due_date(None) is None
for bad in ["2026-02-30", "2026-1-2", "22-10-2026", "hello", 20261022]:
    must_reject(validate_due_date, bad)
print("Test 4 passed: due date")

# 5. Optional tags
assert validate_tags("Study Work") == ["Study", "Work"]
assert validate_tags([" Study ", "Work"]) == ["Study", "Work"]
assert validate_tags("") == []
assert validate_tags([]) == []
assert validate_tags(None) == []
for bad in [["Study", ""], ["Study", 123], 123, {"Study"}]:
    must_reject(validate_tags, bad)
print("Test 5 passed: tags")

# 6. Main/submenu ranges
assert validate_menu_choice("11") == "11"
assert validate_menu_choice(" 3 ") == "3"
for bad in ["12", "-1", "abc", "", "01", None, 3]:
    must_reject(validate_menu_choice, bad)
assert validate_menu_choice("4", ["0", "1", "2", "3", "4"]) == "4"
assert validate_menu_choice("3", ["0", "1", "2", "3"]) == "3"
must_reject(validate_menu_choice, "8", ["0", "1", "2", "3"])
print("Test 6 passed: menu choices")

# 7. Completed status filtering
for value in ["yes", "true", "1", "Y", True]:
    assert validate_completed_filter(value) is True
for value in ["no", "false", "0", "N", False]:
    assert validate_completed_filter(value) is False
for bad in ["maybe", "", None, 2]:
    must_reject(validate_completed_filter, bad)
print("Test 7 passed: completion filter")

# 8. Imported task lists and data
example = [
    {"id": "01", "title": "Homework", "priority": "High",
     "completed": False, "due_date": None, "tags": ["Study"]},
    {"id": "02", "title": "Running", "priority": "Low",
     "completed": True, "due_date": "2026-10-10", "tags": []},
]
cleaned = validate_task_list(example)
assert cleaned == example
assert cleaned is not example
assert validate_task_list([]) == []
bad_id = [dict(example[0], id=1)]
must_reject(validate_task_list, bad_id)
bad_date = [dict(example[0], due_date="2026-02-30")]
must_reject(validate_task_list, bad_date)
bad_priority = [dict(example[0], priority="low")]
must_reject(validate_task_list, bad_priority)
bad_dups = [example[0], dict(example[1], id="1")]
must_reject(validate_task_list, bad_dups)
bad_tag_type = [dict(example[0], tags="Study")]
must_reject(validate_task_list, bad_tag_type)
must_reject(validate_task_list, {"id": "01"})
print("Test 8 passed: imported task data")

print("All validation tests passed!")