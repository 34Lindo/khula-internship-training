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
def list_tasks():
    """List all tasks."""
    storage = TaskStorage()
    tasks = storage.get_all()

    if not tasks:
        click.echo("No tasks found.")
        return

    click.echo("ID | Status | Description | Priority")
    click.echo("---+--------+-------------+---------")

    for task in tasks:
        status = "[x]" if task.completed else "[ ]"

        click.echo(
            f"{task.id} | {status} | "
            f"{task.description} | {task.priority.capitalize()}"
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