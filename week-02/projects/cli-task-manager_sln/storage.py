import json

from task import Task


class TaskStorage:
    """Manage saving and loading tasks from a JSON file."""

    def __init__(self, filename: str = "tasks.json"):
        """Initialize storage and load existing tasks."""
        self.filename = filename
        self.tasks = self.load()

    def load(self) -> list[Task]:
        """Load tasks from the JSON file."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            tasks_data = data.get("tasks", [])

            return [
                Task.from_dict(task_data)
                for task_data in tasks_data
            ]

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []

    def save(self):
        """Save all tasks to the JSON file."""
        data = {
            "tasks": [task.to_dict() for task in self.tasks],
            "next_id": self._get_next_id(),
        }

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    def add(self, task: Task):
        """Add a task and save the updated task list."""
        self.tasks.append(task)
        self.save()

    def delete(self, task_id: int):
        """Delete a task by its ID and save the changes."""
        self.tasks = [
            task for task in self.tasks
            if task.id != task_id
        ]

        self.save()

    def get_all(self) -> list[Task]:
        """Return all stored tasks."""
        return self.tasks

    def get_by_id(self, task_id: int):
        """Return a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def _get_next_id(self) -> int:
        """Return the next available task ID."""
        if not self.tasks:
            return 1

        return max(task.id for task in self.tasks) + 1
