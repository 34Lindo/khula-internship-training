class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root, target_sum):
    """Return True if a root-to-leaf path equals target_sum."""

    if not root:
        return False

    target_sum -= root.val

    if not root.left and not root.right:
        return target_sum == 0

    return (
        has_path_sum(root.left, target_sum)
        or has_path_sum(root.right, target_sum)
    )