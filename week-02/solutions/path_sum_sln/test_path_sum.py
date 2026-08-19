from solution import TreeNode, has_path_sum


def test_path_sum_exists():
    root = TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(
                11,
                TreeNode(7),
                TreeNode(2)
            )
        ),
        TreeNode(
            8,
            TreeNode(13),
            TreeNode(4)
        )
    )

    assert has_path_sum(root, 22) is True


def test_path_sum_does_not_exist():
    root = TreeNode(
        5,
        TreeNode(4),
        TreeNode(8)
    )

    assert has_path_sum(root, 20) is False


def test_empty_tree():
    assert has_path_sum(None, 0) is False


def test_single_node():
    root = TreeNode(1)

    assert has_path_sum(root, 1) is True
    assert has_path_sum(root, 2) is False


def test_path_must_end_at_leaf():
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )

    assert has_path_sum(root, 1) is False