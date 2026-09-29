from storage import savesinfo
from state import details


def f2():  # study hours
    try:
        stdhour = int(input("Enter your today study hour: "))
        x = int(input("Enter your id: "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    for detail in details:
        if detail["id"] == x:
            detail["studyhour"] = stdhour
            savesinfo(details)
            print(f"Your today study hour is {stdhour}.")
            return
    print("ID NOT FOUND")


def f3():  # exam paper strategy
    for detail in details:
        if detail["nature"].lower() == "night":
            print(
                "1. An effective night learner strategy focuses on optimizing your environment\n"
                "2. Managing energy levels\n"
                "3. Applying active recall techniques to stay alert and retain information after dark"
            )
        else:
            print(
                "1. An effective morning routine for learners focuses on waking up the brain\n"
                "2. Protecting focus\n"
                "3. Building steady energy for studying"
            )


def f4():  # study hour management
    print("\n--- Daily Time Planner ---")
    try:
        hours = float(input("Total study hour today: "))
        if hours < 12:
            raw_subjects = input("Enter subjects to study today (comma separated): ")
            subjects = [s.strip() for s in raw_subjects.split(",") if s.strip()]
            if subjects:
                per_subject = hours / len(subjects)
                print(f"\nSuggested Allocation ({per_subject:.2f} hours per subject):")
                for sub in subjects:
                    print(f"- {sub}: {per_subject:.2f} hours")
        else:
            print("Invalid input: Study hours must be less than 12.")
            return
    except ValueError:
        print("Invalid input")
