"""Run with: python -m unittest test_task_operations.py -v"""

import unittest
from task_operations import (
    add_task, modify_task, delete_task, toggle_completed, set_priority
)


class TestTaskOperations(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            {"id": "01", "title": "Homework", "priority": "High",
             "completed": False, "due_date": "2026-10-19", "tags": ["Study"]},
            {"id": "02", "title": "Running", "priority": "Low",
             "completed": True, "due_date": None, "tags": ["Exercise"]},
        ]

    def test_add_task(self):
        new = add_task(self.tasks, "  Read book  ", "Medium", tags=["Leisure"])
        self.assertEqual(new["id"], "03")
        self.assertEqual(new["title"], "Read book")
        self.assertFalse(new["completed"])
        self.assertEqual(len(self.tasks), 3)

    def test_add_without_tags(self):
        self.assertEqual(add_task(self.tasks, "New", "High")["tags"], [])

    def test_add_with_invalid_input(self):
        self.assertIsNone(add_task(self.tasks, "", "High"))
        self.assertIsNone(add_task(self.tasks, "New", "Urgent"))
        self.assertIsNone(add_task(self.tasks, "New", "High", "2026-02-30"))
        self.assertEqual(len(self.tasks), 2)

    def test_string_ids_are_required_for_existing_tasks(self):
        self.tasks[0]["id"] = 1
        self.assertIsNone(add_task(self.tasks, "New", "High"))
        self.assertFalse(delete_task(self.tasks, "01"))

    def test_numeric_strings_with_different_padding_refer_to_same_id(self):
        self.assertTrue(modify_task(self.tasks, "1", {"title": "Changed"}))
        self.assertEqual(self.tasks[0]["title"], "Changed")
        self.assertTrue(delete_task(self.tasks, "02"))

    def test_duplicate_numeric_string_ids_are_rejected(self):
        self.tasks[1]["id"] = "1"
        self.assertIsNone(add_task(self.tasks, "New", "High"))

    def test_new_ids_are_strings_and_keep_two_digits(self):
        self.assertEqual(add_task([], "First", "High")["id"], "01")
        self.assertEqual(add_task(self.tasks, "Third", "High")["id"], "03")

    def test_invalid_string_ids_are_rejected(self):
        for invalid in ("0", "abc", "-1", " 01 ", "1.0", ""):
            self.assertFalse(delete_task(self.tasks, invalid))

    def test_modify_specific_fields(self):
        ok = modify_task(self.tasks, "01", {"title": "Revised", "tags": ["Uni"]})
        self.assertTrue(ok)
        self.assertEqual(self.tasks[0]["title"], "Revised")
        self.assertEqual(self.tasks[0]["priority"], "High")
        self.assertEqual(self.tasks[0]["tags"], ["Uni"])

    def test_modify_is_atomic(self):
        self.assertFalse(modify_task(self.tasks, "01", {
            "title": "Revised", "priority": "Ultra"
        }))
        self.assertEqual(self.tasks[0]["title"], "Homework")

    def test_cannot_modify_id(self):
        self.assertFalse(modify_task(self.tasks, "01", {"id": 42}))
        self.assertEqual(self.tasks[0]["id"], "01")

    def test_delete(self):
        self.assertTrue(delete_task(self.tasks, "01"))
        self.assertEqual(len(self.tasks), 1)
        self.assertFalse(delete_task(self.tasks, "999"))

    def test_toggle_completed(self):
        self.assertTrue(toggle_completed(self.tasks, "01"))
        self.assertTrue(self.tasks[0]["completed"])
        self.assertTrue(toggle_completed(self.tasks, "01"))
        self.assertFalse(self.tasks[0]["completed"])
        self.assertFalse(toggle_completed(self.tasks, "999"))

    def test_set_priority(self):
        self.assertTrue(set_priority(self.tasks, "02", "Medium"))
        self.assertEqual(self.tasks[1]["priority"], "Medium")
        self.assertFalse(set_priority(self.tasks, "02", "urgent"))
        self.assertFalse(set_priority(self.tasks, "10", "High"))

    def test_wrong_id_types(self):
        self.assertFalse(delete_task(self.tasks, 1))
        self.assertFalse(toggle_completed(self.tasks, True))
        self.assertFalse(modify_task(self.tasks, 1, {"title": "Invalid"}))
        self.assertFalse(set_priority(self.tasks, 2, "High"))


if __name__ == "__main__":
    unittest.main()
