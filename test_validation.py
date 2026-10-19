
from validation import validate_title

print(validate_title("  Finish homework  "))

try:
    validate_title("   ")
except ValueError as error:
    print("Successfully rejected invalid title:", error)


from validation import validate_task_id

print(validate_task_id("3"))

for value in ["abc", "0", "-2", ""]:
    try:
        validate_task_id(value)
    except ValueError as error:
        print("Rejected:", value, "-", error)
