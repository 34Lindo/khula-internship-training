import pytest


# --- Data Structure ---

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- Core Implementations ---

def preorder_traversal_recursive(root: TreeNode) -> list[int]:
    """
    Recursive approach (DFS).
    Time Complexity:  O(n) - Visits every node once.
    Space Complexity: O(h) - Call stack depth equals tree height.
    """
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)  # 1. Visit Root
        dfs(node.left)           # 2. Recurse Left
        dfs(node.right)          # 3. Recurse Right

    dfs(root)
    return result


def preorder_traversal_iterative(root: TreeNode) -> list[int]:
    """
    Iterative approach using an explicit Stack (LIFO).
    Time Complexity:  O(n) - Visits every node once.
    Space Complexity: O(h) - Stack stores at most O(h) nodes at a time.
    """
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right FIRST so left is popped and processed FIRST (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result