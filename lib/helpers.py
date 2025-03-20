from db import Session
from db.models import Category, Project, Task

def create_category(session):
    name = input("Enter category name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    category = Category(name=name)
    session.add(category)
    session.commit()
    print("Category created successfully.")

def view_categories(session):
    categories = session.query(Category).all()
    if not categories:
        print("No categories found.")
        return []
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category.name}")
    return categories

def create_project(session):
    categories = view_categories(session)
    if not categories:
        print("Please create a category first.")
        return
    try:
        choice = int(input("Select category by number: ")) - 1
        if 0 <= choice < len(categories):
            category = categories[choice]
            name = input("Enter project name: ").strip()
            if not name:
                print("Name cannot be empty.")
                return
            description = input("Enter project description: ").strip()
            project = Project(name=name, description=description, category=category)
            session.add(project)
            session.commit()
            print("Project created successfully.")
        else:
            print("Invalid category selection.")
    except ValueError:
        print("Please enter a valid number.")

def view_projects(session):
    projects = session.query(Project).all()
    if not projects:
        print("No projects found.")
        return []
    for i, project in enumerate(projects, start=1):
        print(f"{i}. {project.name} (Category: {project.category.name})")
    return projects

def create_task(session):
    projects = view_projects(session)
    if not projects:
        print("Please create a project first.")
        return
    try:
        choice = int(input("Select project by number: ")) - 1
        if 0 <= choice < len(projects):
            project = projects[choice]
            name = input("Enter task name: ").strip()
            if not name:
                print("Name cannot be empty.")
                return
            description = input("Enter task description: ").strip()
            status = input("Enter task status (e.g., Pending, Completed): ").strip() or "Pending"
            task = Task(name=name, description=description, status=status, project=project)
            session.add(task)
            session.commit()
            print("Task created successfully.")
        else:
            print("Invalid project selection.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(session):
    projects = view_projects(session)
    if not projects:
        return
    try:
        choice = int(input("Select project by number to view its tasks: ")) - 1
        if 0 <= choice < len(projects):
            project = projects[choice]
            tasks = project.tasks
            if not tasks:
                print("No tasks found for this project.")
            else:
                for task in tasks:
                    print(f"- {task.name} (Status: {task.status})")
        else:
            print("Invalid project selection.")
    except ValueError:
        print("Please enter a valid number.")

def exit_program(session):
    session.close()  # Clean up session
    print("Goodbye!")
    exit()