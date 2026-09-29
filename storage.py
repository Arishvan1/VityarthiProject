FILENAME = "student_data.txt"


def infooload():
    details = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                criteria = line.split(",")
                if len(criteria) >= 7:
                    detail = {
                        "id": int(criteria[0]),
                        "NAME": criteria[1],
                        "standard": criteria[2],
                        "subject": criteria[3],
                        "result": criteria[4],
                        "nature": criteria[5],
                        "studyhour": int(criteria[6]),
                        "exams": []
                    }

                    if len(criteria) > 7 and criteria[7]:
                        exam_entries = criteria[7].split("|")
                        for entry in exam_entries:
                            parts = entry.split(";")
                            if len(parts) == 4:
                                detail["exams"].append({
                                    "examname": parts[0],
                                    "date": parts[1],
                                    "exampattern": parts[2],
                                    "examtime": parts[3]
                                })

                    details.append(detail)
    except FileNotFoundError:
        pass
    return details


def savesinfo(details):
    """Writes details and exams to student_data.txt."""
    with open(FILENAME, "w") as file:
        for detail in details:
            exams_str = ""
            if "exams" in detail and detail["exams"]:
                exam_list = []
                for ex in detail["exams"]:
                    exam_list.append(
                        f"{ex['examname']};{ex['date']};"
                        f"{ex['exampattern']};{ex['examtime']}"
                    )
                exams_str = "|".join(exam_list)

            line = (
                f"{detail['id']},{detail['NAME']},{detail['standard']},"
                f"{detail['subject']},{detail['result']},{detail['nature']},"
                f"{detail['studyhour']},{exams_str}\n"
            )
            file.write(line)
