import pytest

from task import Task


def test_create_task():
    task = Task(1, "Learn Python")

    assert task.id == 1
    assert task.description == "Learn Python"
    assert task.completed is False
    assert task.priority == "normal"


def test_create_high_priority_task():
    task = Task(2, "Build project", priority="high")

    assert task.priority == "high"


def test_create_low_priority_task():
    task = Task(3, "Read documentation", priority="low")

    assert task.priority == "low"


def test_create_completed_task():
    task = Task(4, "Submit project", completed=True)

    assert task.completed is True


def test_created_at_is_generated():
    task = Task(5, "Test dates")

    assert task.created_at is not None
    assert isinstance(task.created_at, str)


def test_task_to_dict():
    task = Task(1, "Learn Python", priority="high")

    data = task.to_dict()

    assert data["id"] == 1
    assert data["description"] == "Learn Python"
    assert data["completed"] is False
    assert data["priority"] == "high"
    assert "created_at" in data


def test_task_from_dict():
    data = {
        "id": 1,
        "description": "Learn Python",
        "completed": False,
        "priority": "high",
        "created_at": "2026-08-24T10:00:00",
    }

    task = Task.from_dict(data)

    assert task.id == 1
    assert task.description == "Learn Python"
    assert task.completed is False
    assert task.priority == "high"
    assert task.created_at == "2026-08-24T10:00:00"


def test_empty_description_rejected():
    with pytest.raises(ValueError):
        Task(1, "")


def test_whitespace_description_rejected():
    with pytest.raises(ValueError):
        Task(1, "   ")


def test_invalid_priority_rejected():
    with pytest.raises(ValueError):
        Task(1, "Learn Python", priority="urgent")