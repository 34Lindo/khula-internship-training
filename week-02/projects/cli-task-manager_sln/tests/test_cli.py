from click.testing import CliRunner

from cli import cli


def test_add_task():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["add", "Learn Python"],
    )

    assert result.exit_code == 0
    assert "Task added: ID" in result.output


def test_add_high_priority_task():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["add", "Build project", "--priority", "high"],
    )

    assert result.exit_code == 0
    assert "Task added: ID" in result.output


def test_add_low_priority_task():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["add", "Read documentation", "--priority", "low"],
    )

    assert result.exit_code == 0
    assert "Task added: ID" in result.output


def test_add_invalid_priority():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["add", "Invalid priority", "--priority", "urgent"],
    )

    assert result.exit_code != 0
    assert "Invalid value" in result.output


def test_list_tasks():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["list"],
    )

    assert result.exit_code == 0


def test_list_empty_tasks():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["list"],
    )

    assert result.exit_code == 0


def test_done_task():
    runner = CliRunner()

    add_result = runner.invoke(
        cli,
        ["add", "Task to complete"],
    )

    assert add_result.exit_code == 0

    # Get the ID assigned by the application.
    task_id = add_result.output.strip().split()[-1]

    result = runner.invoke(
        cli,
        ["done", task_id],
    )

    assert result.exit_code == 0
    assert "marked as complete" in result.output


def test_done_invalid_task():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["done", "99999"],
    )

    assert result.exit_code == 0
    assert "not found" in result.output


def test_delete_task():
    runner = CliRunner()

    add_result = runner.invoke(
        cli,
        ["add", "Task to delete"],
    )

    assert add_result.exit_code == 0

    # Get the ID assigned by the application.
    task_id = add_result.output.strip().split()[-1]

    result = runner.invoke(
        cli,
        ["delete", task_id],
    )

    assert result.exit_code == 0
    assert "deleted" in result.output


def test_delete_invalid_task():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["delete", "99999"],
    )

    assert result.exit_code == 0
    assert "not found" in result.output