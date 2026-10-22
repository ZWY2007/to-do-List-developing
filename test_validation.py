from validation import (validate_title, validate_task_id,
                        validate_priority, validate_due_date,
                        validate_tags, validate_menu_choice)


# Test 1: title
assert validate_title("  Finish homework  ") == "Finish homework"
for value in ["", "   ", None, 123]:
    try:
        validate_title(value)
        raise AssertionError("Invalid title was accepted")
    except ValueError:
        print("Rejected invalid title:", value)
print("Test 1 passed: title")


# Test 2: task ID
assert validate_task_id("3") == 3
assert validate_task_id(" 5 ") == 5
assert validate_task_id(2) == 2
for value in ["abc", "0", "-2", "", None, True, 1.5]:
    try:
        validate_task_id(value)
        raise AssertionError("Invalid task ID was accepted")
    except ValueError:
        print("Rejected invalid ID:", value)
print("Test 2 passed: task ID")


# Test 3: priority
assert validate_priority("High") == "High"
assert validate_priority(" high ") == "High"
assert validate_priority("MEDIUM") == "Medium"
assert validate_priority("low") == "Low"
for value in ["Urgent", "", "  ", None, 123]:
    try:
        validate_priority(value)
        raise AssertionError("Invalid priority was accepted")
    except ValueError:
        print("Rejected invalid priority:", value)
print("Test 3 passed: priority")


# Test 4: due date
assert validate_due_date("2026-10-22") == "2026-10-22"
assert validate_due_date(" 2026-12-01 ") == "2026-12-01"
assert validate_due_date("") is None
assert validate_due_date(None) is None
for value in ["2026-02-30", "2026-1-2", "22-10-2026", "hello", 20261022]:
    try:
        validate_due_date(value)
        raise AssertionError("Invalid due date was accepted")
    except ValueError:
        print("Rejected invalid due date:", value)
print("Test 4 passed: due date")


# Test 5: tags
assert validate_tags("Study Work") == ["Study", "Work"]
assert validate_tags([" Study ", "Work"]) == ["Study", "Work"]
assert validate_tags("") == []
assert validate_tags([]) == []
assert validate_tags(None) == []
for value in [["Study", ""], ["Study", 123], 123, {"Study"}]:
    try:
        validate_tags(value)
        raise AssertionError("Invalid tags were accepted")
    except ValueError:
        print("Rejected invalid tags:", value)
print("Test 5 passed: tags")


# Test 6: main menu choice
assert validate_menu_choice("0") == "0"
assert validate_menu_choice(" 3 ") == "3"
assert validate_menu_choice("10") == "10"
assert validate_menu_choice("11") == "11"
for value in ["12", "-1", "abc", "", "01", None, 3]:
    try:
        validate_menu_choice(value)
        raise AssertionError("Invalid menu choice was accepted")
    except ValueError:
        print("Rejected invalid menu choice:", value)
print("Test 6 passed: menu choice")

print("All validation tests passed!")