# TaskMaster CLI

TaskMaster is a command-line task management system built with Python and SQLAlchemy. It allows users to organize tasks into projects and categorize them, providing a simple yet effective way to manage work or personal activities.

## Installation
1. Clone the repository: `git clone <your-repo-url>`
2. Navigate to the directory: `cd taskmaster`
3. Install dependencies: `pipenv install`
4. Activate the virtual environment: `pipenv shell`
5. Run the CLI: `python lib/cli.py`

## Features
- Manage categories to group projects.
- Create and view projects within categories.
- Add and view tasks within projects, with status tracking.

## File Structure
- **lib/cli.py**: Main CLI script with menu-driven interface.
  - `main()`: Runs the main loop and displays the top-level menu.
  - `category_menu()`, `project_menu()`, `task_menu()`: Submenus for entity management.
- **lib/helpers.py**: Helper functions for CRUD operations.
  - `create_category()`, `create_project()`, `create_task()`: Create new entities.
  - `view_categories()`, `view_projects()`, `view_tasks()`: Display existing entities.
  - `exit_program()`: Closes the session and exits gracefully.
- **lib/db/models.py**: Defines SQLAlchemy models (`Category`, `Project`, `Task`) with relationships.
- **lib/db/__init__.py**: Sets up the database engine and session.

## Usage
Run `python lib/cli.py` and follow the prompts to:
1. Create categories (e.g., "Work").
2. Add projects to categories (e.g., "Website Redesign").
3. Add tasks to projects (e.g., "Design Homepage", status "Pending").
4. View your organized tasks and projects.