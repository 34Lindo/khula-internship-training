def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to the target.

    Args:
        numbers (list[int]): List of integers.
        target (int): Target sum.

    Returns:
        list[int]: Indices of the two numbers.
    """
    seen = {}

    for index, number in enumerate(numbers):
        complement = target - number

        if complement in seen:
            return [seen[complement], index]

        seen[number] = index

    return []