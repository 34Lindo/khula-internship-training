# Exercise 2: Palindrome Number

**Difficulty:** Easy
**Topics:** Number Operations, Validation
**Estimated Time:** 30-45 minutes

## Problem Statement

Given an integer `x`, return `True` if `x` is a palindromic number, and `False` otherwise.

A palindromic number reads the same forward and backward (e.g., 121 is a palindrome, 123 is not).

**Note:** Negative numbers are not palindromes.

### Examples

**Input:** `x = 121`
**Output:** `True`

**Input:** `x = -121`
**Output:** `False`

**Input:** `x = 10`
**Output:** `False`

## Approach 1: String Conversion (Simpler)

Convert the number to a string and check if it reads the same backwards:

1. Handle negative numbers (return False)
2. Convert to string
3. Compare with reversed string

## Approach 2: Mathematical (More Elegant)

Reverse the number mathematically without converting to string:

1. Handle negative numbers
2. Reverse the digits using modulo and division
3. Compare with original

**Hint:** Use `x % 10` to get the last digit and `x // 10` to remove it.

## Implementation

```python
def is_palindrome(x: int) -> bool:
    """
    Determine if an integer is a palindrome.

    Args:
        x: The integer to check

    Returns:
        True if x is a palindrome, False otherwise
    """
    # Your solution here
    pass
```

## Test Cases

```python
def test_palindrome():
    # Basic palindromes
    assert is_palindrome(121) == True
    assert is_palindrome(1) == True
    assert is_palindrome(0) == True

    # Not palindromes
    assert is_palindrome(-121) == False
    assert is_palindrome(10) == False
    assert is_palindrome(123) == False

    # Edge cases
    assert is_palindrome(-1) == False
    assert is_palindrome(9) == True
    assert is_palindrome(1001) == True
    assert is_palindrome(1000) == False

    print("All tests passed!")

if __name__ == "__main__":
    test_palindrome()
```

## Learning Goals

By completing this exercise, you'll understand:

- How to work with number operations (modulo, division)
- How to reverse a number mathematically
- Two different approaches to solving the same problem
- Trade-offs between simplicity and efficiency

## Complexity Analysis

**Approach 1 (String):**

- Time Complexity: O(log n) - where n is the number of digits
- Space Complexity: O(log n) - for the string conversion

**Approach 2 (Mathematical):**

- Time Complexity: O(log n) - where n is the number of digits
- Space Complexity: O(1) - only using variables

## Edge Cases to Consider

- Single digit numbers (always palindromes)
- Negative numbers (never palindromes)
- Numbers ending in 0 (10, 100 are not palindromes)
- Very large numbers

## Follow-up Questions

1. Which approach do you prefer and why?
2. Can you implement both approaches?
3. Does the string approach technically work with negative numbers? Why not?
4. What's the largest number you could check?

## Mentor Notes

Common mistakes:

- Forgetting to handle negative numbers
- Not understanding why 10 is not a palindrome (reversed would be 01 = 1)
- Confusion between string reversal and number reversal

Teaching moments:

- Discuss why there are multiple valid approaches
- Explore trade-offs: readability vs. space efficiency
- Ask which approach they prefer and why
