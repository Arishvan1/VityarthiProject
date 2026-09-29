from students import f1
from study import f2, f3, f4
from exams import f5


print("____STUDY MANAGEMENT SYSTEM___")

choice = " "
while choice != "6":
    print("\n1. Add details")
    print("2. Add study hours")
    print("3. View exam prep strategy")
    print("4. Time dividing")
    print("5. Schedule exam")
    print("6. EXIT")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        f1()
    elif choice == "2":
        f2()
    elif choice == "3":
        f3()
    elif choice == "4":
        f4()
    elif choice == "5":
        f5()
    elif choice == "6":
        print("Exiting application...")
        break
    else:
        print("Invalid choice")
