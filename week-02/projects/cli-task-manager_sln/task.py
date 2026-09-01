from datetime import datetime


class Task:
    """Represent a single task."""

    VALID_PRIORITIES = {"low", "normal", "high"}

    def __init__(
        self,
        id: int,
        description: str,
        completed: bool = False,
        priority: str = "normal",
        created_at: str | None = None,
    ):
        if not description.strip():
            raise ValueError("Task description cannot be empty.")

        if priority not in self.VALID_PRIORITIES:
            raise ValueError(
                "Priority must be low, normal, or high."
            )

        self.id = id
        self.description = description
        self.completed = completed
        self.priority = priority
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        """Convert the task into a dictionary."""
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "priority": self.priority,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task from a dictionary."""
        return cls(
            id=data["id"],
            description=data["description"],
            completed=data.get("completed", False),
            priority=data.get("priority", "normal"),
            created_at=data.get("created_at"),
        )