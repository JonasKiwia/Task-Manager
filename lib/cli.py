from helpers import (
    create_category, view_categories,
    create_project, view_projects,
    create_task, view_tasks,
    exit_program
)
from db import Session

def main():
    session = Session()
    while True:
        print("\n=== TaskMaster ===")
        print("1. Manage Categories")
        print("2. Manage Projects")
        print("3. Manage Tasks")
        print("0. Exit")
        choice = input("> ").strip()
        if choice == "0":
            exit_program(session)
        elif choice == "1":
            category_menu(session)
        elif choice == "2":
            project_menu(session)
        elif choice == "3":
            task_menu(session)
        else:
            print("Invalid choice. Please try again.")

def category_menu(session):
    while True:
        print("\nCategory Management:")
        print("1. Create a category")
        print("2. View all categories")
        print("0. Back to main menu")
        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            create_category(session)
        elif choice == "2":
            view_categories(session)
        else:
            print("Invalid choice.")

def project_menu(session):
    while True:
        print("\nProject Management:")
        print("1. Create a project")
        print("2. View all projects")
        print("0. Back to main menu")
        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            create_project(session)
        elif choice == "2":
            view_projects(session)
        else:
            print("Invalid choice.")

def task_menu(session):
    while True:
        print("\nTask Management:")
        print("1. Create a task")
        print("2. View tasks of a project")
        print("0. Back to main menu")
        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice == "1":
            create_task(session)
        elif choice == "2":
            view_tasks(session)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()