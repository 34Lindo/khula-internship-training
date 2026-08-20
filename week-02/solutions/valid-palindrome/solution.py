def isPalindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome,
    considering only alphanumeric characters and ignoring case.
    """

    left = 0
    right = len(s) - 1

    while left < right:

        # Move left forward if the character is not alphanumeric
        while left < right and not s[left].isalnum():
            left += 1

        # Move right backward if the character is not alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare the two valid characters
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True