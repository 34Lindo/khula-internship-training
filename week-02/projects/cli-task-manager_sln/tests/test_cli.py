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


def test_list_pending_tasks():
    runner = CliRunner()

    runner.invoke(cli, ["add", "Pending task"])

    result = runner.invoke(
        cli,
        ["list", "--status", "pending"],
    )

    assert result.exit_code == 0
    assert "Pending task" in result.output


def test_list_completed_tasks():
    runner = CliRunner()

    add_result = runner.invoke(
        cli,
        ["add", "Completed task"],
    )

    assert add_result.exit_code == 0

    task_id = add_result.output.strip().split()[-1]

    done_result = runner.invoke(
        cli,
        ["done", task_id],
    )

    assert done_result.exit_code == 0

    result = runner.invoke(
        cli,
        ["list", "--status", "completed"],
    )

    assert result.exit_code == 0
    assert "Completed task" in result.output


def test_edit_task():
    runner = CliRunner()

    add_result = runner.invoke(
        cli,
        ["add", "Old description"],
    )

    assert add_result.exit_code == 0

    task_id = add_result.output.strip().split()[-1]

    result = runner.invoke(
        cli,
        ["edit", task_id, "New description"],
    )

    assert result.exit_code == 0
    assert "updated" in result.output

    list_result = runner.invoke(
        cli,
        ["list"],
    )

    assert "New description" in list_result.output
    assert "Old description" not in list_result.output


def test_edit_task_priority():
    runner = CliRunner()

    add_result = runner.invoke(
        cli,
        ["add", "Task to edit"],
    )

    assert add_result.exit_code == 0

    task_id = add_result.output.strip().split()[-1]

    result = runner.invoke(
        cli,
        [
            "edit",
            task_id,
            "High priority task",
            "--priority",
            "high",
        ],
    )

    assert result.exit_code == 0
    assert "updated" in result.output

    list_result = runner.invoke(
        cli,
        ["list"],
    )

    assert "High priority task" in list_result.output
    assert "High" in list_result.output


def test_edit_invalid_task():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["edit", "99999", "Updated task"],
    )

    assert result.exit_code == 0
    assert "not found" in result.output


def test_search_task():
    runner = CliRunner()

    add_result = runner.invoke(
        cli,
        ["add", "Learn Python programming"],
    )

    assert add_result.exit_code == 0

    result = runner.invoke(
        cli,
        ["search", "Python"],
    )

    assert result.exit_code == 0
    assert "Learn Python programming" in result.output


def test_search_is_case_insensitive():
    runner = CliRunner()

    add_result = runner.invoke(
        cli,
        ["add", "Learn Python"],
    )

    assert add_result.exit_code == 0

    result = runner.invoke(
        cli,
        ["search", "python"],
    )

    assert result.exit_code == 0
    assert "Learn Python" in result.output


def test_search_no_results():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["search", "something-that-does-not-exist"],
    )

    assert result.exit_code == 0
    assert "No tasks found." in result.output
