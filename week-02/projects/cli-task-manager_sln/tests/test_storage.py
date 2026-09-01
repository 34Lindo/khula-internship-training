import json

from task import Task
from storage import TaskStorage


def test_storage_starts_empty_when_file_does_not_exist(tmp_path):
    filename = tmp_path / "tasks.json"

    storage = TaskStorage(str(filename))

    assert storage.get_all() == []


def test_add_task(tmp_path):
    filename = tmp_path / "tasks.json"
    storage = TaskStorage(str(filename))

    task = Task(1, "Learn Python")

    storage.add(task)

    tasks = storage.get_all()

    assert len(tasks) == 1
    assert tasks[0].description == "Learn Python"


def test_save_and_load_tasks(tmp_path):
    filename = tmp_path / "tasks.json"

    storage = TaskStorage(str(filename))

    task = Task(1, "Build Task Manager", priority="high")
    storage.add(task)

    new_storage = TaskStorage(str(filename))

    tasks = new_storage.get_all()

    assert len(tasks) == 1
    assert tasks[0].id == 1
    assert tasks[0].description == "Build Task Manager"
    assert tasks[0].priority == "high"


def test_completed_task_is_saved(tmp_path):
    filename = tmp_path / "tasks.json"

    storage = TaskStorage(str(filename))

    task = Task(1, "Submit project", completed=True)
    storage.add(task)

    new_storage = TaskStorage(str(filename))

    assert new_storage.get_all()[0].completed is True


def test_multiple_tasks_are_saved(tmp_path):
    filename = tmp_path / "tasks.json"

    storage = TaskStorage(str(filename))

    storage.add(Task(1, "Learn Python"))
    storage.add(Task(2, "Build project"))
    storage.add(Task(3, "Write tests"))

    new_storage = TaskStorage(str(filename))

    tasks = new_storage.get_all()

    assert len(tasks) == 3
    assert tasks[0].description == "Learn Python"
    assert tasks[1].description == "Build project"
    assert tasks[2].description == "Write tests"


def test_delete_task(tmp_path):
    filename = tmp_path / "tasks.json"

    storage = TaskStorage(str(filename))

    storage.add(Task(1, "Learn Python"))
    storage.add(Task(2, "Build project"))

    storage.delete(1)

    tasks = storage.get_all()

    assert len(tasks) == 1
    assert tasks[0].id == 2


def test_delete_task_is_persisted(tmp_path):
    filename = tmp_path / "tasks.json"

    storage = TaskStorage(str(filename))

    storage.add(Task(1, "Learn Python"))
    storage.add(Task(2, "Build project"))

    storage.delete(1)

    new_storage = TaskStorage(str(filename))

    tasks = new_storage.get_all()

    assert len(tasks) == 1
    assert tasks[0].id == 2


def test_corrupted_json_returns_empty_list(tmp_path):
    filename = tmp_path / "tasks.json"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("this is not valid JSON")

    storage = TaskStorage(str(filename))

    assert storage.get_all() == []


def test_tasks_json_has_correct_structure(tmp_path):
    filename = tmp_path / "tasks.json"

    storage = TaskStorage(str(filename))

    storage.add(Task(1, "Learn Python", priority="high"))

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert "tasks" in data
    assert "next_id" in data
    assert len(data["tasks"]) == 1
    assert data["tasks"][0]["id"] == 1


def test_next_id_is_correct(tmp_path):
    filename = tmp_path / "tasks.json"

    storage = TaskStorage(str(filename))

    storage.add(Task(1, "First task"))
    storage.add(Task(2, "Second task"))

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data["next_id"] == 3
