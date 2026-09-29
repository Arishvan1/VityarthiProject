from storage import savesinfo
from state import details


def f5():  # schedule exam
    try:
        x = int(input("Enter student id: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    for detail in details:
        if detail["id"] == x:
            if "exams" not in detail:
                detail["exams"] = []

            exname = input("Enter Exam Name: ")
            exdate = input("Enter Exam Date (YYYY-MM-DD): ")
            expattern = input(
                "Enter total no of ques and marks pattern (ques/marks): "
            )
            time = input("Enter time for exam: ")

            detail["exams"].append({
                "examname": exname,
                "date": exdate,
                "exampattern": expattern,
                "examtime": time
            })

            savesinfo(details)
            print(f"Exam '{exname}' scheduled and saved to file!")
            return
    print("ID NOT FOUND")
