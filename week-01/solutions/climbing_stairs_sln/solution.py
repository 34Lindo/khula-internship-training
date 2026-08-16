def climb_stairs(n: int) -> int:
    """
    Calculate the number of distinct ways to climb n stairs.

    Each move can be either 1 or 2 stairs.

    Args:
        n (int): Number of stairs.

    Returns:
        int: Number of distinct ways to reach the top.
    """
    if n <= 2:
        return n

    one_step = 1
    two_steps = 2

    for _ in range(3, n + 1):
        next_steps = one_step + two_steps
        one_step = two_steps
        two_steps = next_steps

    return two_steps