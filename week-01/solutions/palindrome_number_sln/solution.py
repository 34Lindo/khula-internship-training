def reverse_number(number: int) -> int:
    """
    Reverse the digits of an integer.

    Args:
        number (int): The integer to reverse.

    Returns:
        int: The reversed integer.
    """
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return reversed_number


def is_palindrome(number: int) -> bool:
    """
    Check whether an integer is a palindrome.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is a palindrome, otherwise False.
    """
    if number < 0:
        return False

    original = number
    reversed_number = reverse_number(number)

    return original == reversed_number