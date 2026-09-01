# Task Manager CLI

A command-line task management application built with Python and Click.

The application allows users to create, view, update, complete, delete, search, and filter tasks. Tasks are automatically persisted to a JSON file.

## Features

### Core Features

- Add tasks
- List tasks
- Mark tasks as complete
- Delete tasks
- Persist tasks to `tasks.json`

### Additional Features

- Filter tasks by status
- Filter tasks by priority
- Edit existing tasks
- Search tasks
- Clear all tasks
- Task creation timestamps
- Input validation
- Corrupted JSON handling
- Invalid task ID handling

## Project Structure

```text
cli-task-manager_sln/
├── main.py
├── task.py
├── storage.py
├── cli.py
├── tasks.json
├── requirements.txt
├── .gitignore
├── README.md
└── tests/
    ├── test_task.py
    ├── test_storage.py
    └── test_cli.py
```
