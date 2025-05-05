from controllers.student_controller import StudentController
from controllers.admin_controller import AdminController

RESET = '\033[0m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'

def run_cli():
    while True:
        print(f"{CYAN}University System:  (A)dmin,  (S)tudent, or X : {RESET}", end="")
        choice = input().strip().lower()

        if choice == 's':
            student_menu()
        elif choice == 'a':
            admin_menu()
        elif choice == 'x':
            print(f"\t{YELLOW}Thank You{RESET}")
            break
        else:
            print(f"{RED}Invalid option.{RESET}")

def student_menu():
    controller = StudentController()
    while True:
        print(f"\t{CYAN}Student System (l/r/x): {RESET}", end="")
        choice = input().strip().lower()

        if choice == 'r':
            print(f"{GREEN}Student Sign Up{RESET}")
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            success, message = controller.register(name, email, password)
            print(message)

        elif choice == 'l':
            print(f"{GREEN}Student Sign In{RESET}")
            email = input("Email: ")
            password = input("Password: ")
            student, message = controller.login(email, password)
            print(message)
            if student:
                student_course_menu(controller, student)

        elif choice == 'x':
            break
        else:
            print(f"{RED}Invalid option.{RESET}")

def student_course_menu(controller, student):
    while True:
        print(f"\t{CYAN}Student Course Menu:{RESET}")
        print("\t(C)hange password")
        print("\t(E)nrol in subject")
        print("\t(R)emove subject")
        print("\t(S)how subjects")
        print("\t(X)exit")
        choice = input().strip().lower()

        if choice == 'c':
            new_pass = input("Enter new password: ")
            success, message = controller.change_password(student, new_pass)
            print(message)

        elif choice == 'e':
            success, message = controller.enrol_subject(student)
            print(message)

        elif choice == 'r':
            sub_id = input("Enter subject ID to remove: ")
            success, message = controller.remove_subject(student, sub_id)
            print(message)

        elif choice == 's':
            print(controller.show_subjects(student))

        elif choice == 'x':
            break
        else:
            print(f"{RED}Invalid option.{RESET}")

def admin_menu():
    controller = AdminController()
    while True:
        print(f"\t{CYAN}Admin System (c/g/p/r/s/x): {RESET}", end="")
        choice = input().strip().lower()

        if choice == 's':
            students = controller.show_all()
            if not students or students == ["< Nothing to Display >"]:
                print("< Nothing to Display >")
            else:
                for s in students:
                    print(s)

        elif choice == 'g':
            groups = controller.group_by_grade()
            if not groups or groups == {"< Nothing to Display >": []}:
                print("< Nothing to Display >")
            else:
                print("Grade Grouping")
                for grade, names in sorted(groups.items()):
                    print(f"{grade} --> [{', '.join(names)}]")

        elif choice == 'p':
            passed, failed = controller.partition_pass_fail()
            if not passed and not failed:
                print("< Nothing to Display >")
            else:
                print("PASS/FAIL Partition")
                print("FAIL -->")
                print("\n".join(failed) if failed else "None")
                print("PASS -->")
                print("\n".join(passed) if passed else "None")

        elif choice == 'r':
            sid = input("Remove by ID: ").strip()
            if controller.remove_by_id(sid):
                print(f"Removing Student {sid} Account")
            else:
                print(f"Student {sid} does not exist")

        elif choice == 'c':
            confirm = input("Are you sure you want to clear the database (Y)ES/(N)O: ").strip().lower()
            if confirm == 'y':
                controller.clear_all()
                print("Students data cleared")

        elif choice == 'x':
            break
        else:
            print(f"{RED}Invalid option.{RESET}")
