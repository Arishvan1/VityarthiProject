from storage import savesinfo
from state import details


def f1():  # Add details
    print("\n--- Add Student Details ---")
    try:
        student_id = int(input("Enter Your id: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    for detail in details:
        if detail["id"] == student_id:
            print(f"Error: A student with ID {student_id} already exists.")
            return

    name = input("Enter Your Name: ")
    standard = input("Enter the class: ")
    sub = input("Enter the subjects: ")
    result = input("Enter your result: ")
    nature = input("Enter your study pattern (night/morning): ")

    detail = {
        "id": student_id,
        "NAME": name,
        "standard": standard,
        "subject": sub,
        "result": result,
        "nature": nature,
        "studyhour": 0,
        "exams": []
    }

    details.append(detail)
    savesinfo(details)
    print(f"ID {student_id} saved to file!")
