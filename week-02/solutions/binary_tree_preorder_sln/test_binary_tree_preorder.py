# --- Automated Test Suite ---
from solution import TreeNode, preorder_traversal_recursive, preorder_traversal_iterative
def test_preorder_standard_tree():
    """
    Tree structure:
        1
         \
          2
         /
        3
    """
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    expected = [1, 2, 3]
    assert preorder_traversal_recursive(root) == expected
    assert preorder_traversal_iterative(root) == expected


def test_preorder_empty_tree():
    assert preorder_traversal_recursive(None) == []
    assert preorder_traversal_iterative(None) == []


def test_preorder_single_node():
    root = TreeNode(1)
    assert preorder_traversal_recursive(root) == [1]
    assert preorder_traversal_iterative(root) == [1]


def test_preorder_full_binary_tree():
    """
         1
       /   \
      2     3
     / \
    4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)

    expected = [1, 2, 4, 5, 3]
    assert preorder_traversal_recursive(root) == expected
    assert preorder_traversal_iterative(root) == expected