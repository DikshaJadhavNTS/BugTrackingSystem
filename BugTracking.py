from MainDict import *

def main_menu():
    while True:
        print("\n*********************** Bug Tracking System***************************")
        print("1. Display Bugs and Developers")
        print("2. Add New Bug")
        print("3. Assign Bugs to Developers")
        print("4. Update Bug Status")
        print("5. Filter Bugs (Severity/Status)")
        print("6. Developer Dashboard")
        print("7. Find Similar Bugs")
        print("8. Detect Stale Bugs")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Display()
        elif choice == "2":
            add_new_bug(bugs)
        elif choice == "3":
            bug_assigner()
        elif choice == "4":
            UpdateStatus()
        elif choice == "5":
            filter_bugs()
        elif choice == "6":
            developer_dashboard()
        elif choice == "7":
            SimilarBugs()
        elif choice == "8":
            DetectBugs()
        elif choice == "9":
            print("Exiting Bug Tracking System")
            break
        else:
            print("Invalid choice. Please try again.")
            break

if __name__ == "__main__":
    main_menu()
