import click

from storage import TaskStorage
from task import Task


@click.group()
def cli():
    """Task Manager CLI."""
    pass


@cli.command()
@click.argument("description")
@click.option(
    "--priority",
    type=click.Choice(["low", "normal", "high"]),
    default="normal",
)
def add(description, priority):
    """Add a new task."""
    storage = TaskStorage()

    task_id = storage._get_next_id()

    task = Task(
        id=task_id,
        description=description,
        priority=priority,
    )

    storage.add(task)

    click.echo(f"Task added: ID {task.id}")


@cli.command(name="list")
@click.option(
    "--status",
    type=click.Choice(["pending", "completed"]),
    default=None,
)
@click.option(
    "--priority",
    type=click.Choice(["low", "normal", "high"]),
    default=None,
)
def list_tasks(status, priority):
    """List tasks with optional filters."""
    storage = TaskStorage()
    tasks = storage.get_all()

    if status == "pending":
        tasks = [
            task for task in tasks
            if not task.completed
        ]

    elif status == "completed":
        tasks = [
            task for task in tasks
            if task.completed
        ]

    if priority is not None:
        tasks = [
            task for task in tasks
            if task.priority == priority
        ]

    if not tasks:
        click.echo("No tasks found.")
        return

    click.echo("ID | Status | Description | Priority")
    click.echo("---+--------+-------------+---------")

    for task in tasks:
        task_status = "[x]" if task.completed else "[ ]"

        click.echo(
            f"{task.id} | {task_status} | "
            f"{task.description} | "
            f"{task.priority.capitalize()}"
        )


@cli.command()
@click.argument("task_id", type=int)
def done(task_id):
    """Mark a task as complete."""
    storage = TaskStorage()

    task = storage.get_by_id(task_id)

    if task is None:
        click.echo(f"Task {task_id} not found.")
        return

    task.completed = True
    storage.save()

    click.echo(f"✓ Task {task_id} marked as complete")


@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete a task."""
    storage = TaskStorage()

    task = storage.get_by_id(task_id)

    if task is None:
        click.echo(f"Task {task_id} not found.")
        return

    storage.delete(task_id)

    click.echo(f"✓ Task {task_id} deleted")


@cli.command()
@click.argument("task_id", type=int)
@click.argument("description")
@click.option(
    "--priority",
    type=click.Choice(["low", "normal", "high"]),
    default=None,
)
def edit(task_id, description, priority):
    """Edit an existing task."""
    storage = TaskStorage()

    task = storage.get_by_id(task_id)

    if task is None:
        click.echo(f"Task {task_id} not found.")
        return

    if not description.strip():
        click.echo("Task description cannot be empty.")
        return

    task.description = description

    if priority is not None:
        task.priority = priority

    storage.save()

    click.echo(f"✓ Task {task_id} updated")


@cli.command()
@click.argument("query")
def search(query):
    """Search tasks by description."""
    storage = TaskStorage()
    tasks = storage.get_all()

    query = query.strip().lower()

    if not query:
        click.echo("Search query cannot be empty.")
        return

    results = [
        task for task in tasks
        if query in task.description.lower()
    ]

    if not results:
        click.echo("No tasks found.")
        return

    click.echo("ID | Status | Description | Priority")
    click.echo("---+--------+-------------+---------")

    for task in results:
        task_status = "[x]" if task.completed else "[ ]"

        click.echo(
            f"{task.id} | {task_status} | "
            f"{task.description} | "
            f"{task.priority.capitalize()}"
        )
@cli.command()
@click.option(
    "--confirm",
    is_flag=True,
    help="Confirm that all tasks should be deleted.",
)
def clear(confirm):
    """Delete all tasks."""
    if not confirm:
        click.echo("Use --confirm to delete all tasks.")
        return

    storage = TaskStorage()

    storage.tasks = []
    storage.save()

    click.echo("✓ All tasks deleted.")