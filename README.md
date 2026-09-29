# VityarthiProject
Study Management Program
#1.Project Overview: My Project is a Study Management System made using a Python-based console application that helps students maintain basic academic information and organize their study activities. This system stores details in text files and provides options for saving study hours, understanding study pattern strategies, dividing available study time among various subjects, and scheduling examinations.
# 2. Project Structure
- `main.py` - starts the program and then displays main menu
- `storage.py` - handles loading and storing student information.
- `state.py` - print the shared student data at staring the program.
- `students.py` - Contains student-detail functionality (`f1`).
- `study.py` - Contains study-hour, strategy, and time-planning functions (`f2`, `f3`, `f4`).
- `exams.py` - Contains exam scheduling (`f5`).
- `student_data.txt` - database used by programmer.
- `requirements.txt` - required information which are needed to execute the program.
- `Final_Report.docx` - Project report containing explanation, complete source code, and sample output.
# 3. How to Run
1. Install Python 3.8 or later.
2. Keep all `.py` files and `student_data.txt` in the same folder.
3. Open Command Prompt/Terminal in the project folder.
4. Run:
   `python main.py`

# 4. Menu
1. Add details
2. Add study hours
3. View exam prep strategy
4. Time dividing
5. Schedule exam
6. Exit

# 5. Data Storage
The program uses `student_data.txt`. Each student record contains student ID, name, class, subject, result, study pattern, study hours, and optional examination information.
